from flask import Flask, jsonify, request
from datetime import datetime, timezone
import uuid
import socket
import os

app = Flask(__name__)

PRODUCT = "Foundry"
SERVICE = "foundry"
VERSION = "0.0.2"
PUBLIC_HOST = os.environ.get("FOUNDRY_PUBLIC_HOST", socket.gethostname())

VMS = {}
CONSOLES = {}

def now_utc():
    return datetime.now(timezone.utc).isoformat()

def make_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

@app.get("/v1/ping")
def ping():
    return jsonify({
        "product": PRODUCT,
        "service": SERVICE,
        "version": VERSION,
        "status": "OK",
        "time": now_utc()
    })

@app.get("/v1/vms")
def list_vms():
    kind = request.args.get("kind")

    vms = list(VMS.values())
    if kind:
        vms = [vm for vm in vms if vm.get("kind") == kind]

    return jsonify({
        "status": "ok",
        "vms": vms
    })

@app.post("/v1/vms")
def create_vm():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    kind = data.get("kind", "shim")

    if not name:
        return jsonify({
            "status": "error",
            "error": "missing required field: name"
        }), 400

    vm_id = make_id("vm")
    console_id = make_id("console")

    vm = {
        "id": vm_id,
        "name": name,
        "kind": kind,
        "host": PUBLIC_HOST,
        "status": "stopped",
        "console": console_id,
        "created_at": now_utc()
    }

    console = {
        "id": console_id,
        "title": f"{name} console",
        "vm_id": vm_id,
        "vm_name": name,
        "state": "available",
        "host": PUBLIC_HOST,
        "port": 8765,
        "created_at": now_utc()
    }

    VMS[vm_id] = vm
    CONSOLES[console_id] = console

    return jsonify({
        "status": "ok",
        "vm": vm,
        "console": console
    }), 201

@app.get("/v1/consoles")
def list_consoles():
    return jsonify({
        "status": "ok",
        "consoles": list(CONSOLES.values())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5606)
