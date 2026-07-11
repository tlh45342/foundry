# foundry
Virtualization Environment


This will be to support a virtualization environment.

This will will a number of tools.

NOTE: t32 is a small instruction set designed around keeping things small and manageable.
using t32 is helps as a lanch board with my large efforts to virtualize ARM and x86/x64.
virtualizaing the larger more commericial items is not a small task.  This allows us to create a smaller elephant to consume and work with.

foundry = virualization
  foundry - the giant orchestrator in the sky
  t32 ISA architecture
  vconsole - may disappear and be consumed but for now I tracking seperately.
  switchyard - a platform for faux networking.  Useful for testing.  might tie it to real networks later with ipsec tunnels.  but for now this is a pipe dream.

guppy   - disk/image management
t32-asm - tiny-32 ISA assembler
t32-cc  - tiny-32 c compiler (this is largely a shim at the moment)
vmctrl  - a cli tool used to controling vm
