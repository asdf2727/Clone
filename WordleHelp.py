import CmdProcessor as cp

print("Welcome to Wordle collector!")
cmdProcessor = cp.CmdProcessor()
while True:
    while True:
        line = input("> ").lower()
        args = line.split()
        if len(args) > 0:
            break
    cmd = args[0]
    args.pop(0)
    force = False
    if "--force" in args:
        force = True
        args.pop(args.index("--force"))
    
    if cmd == "quit" or cmd == "exit":
        if cmdProcessor.processExit():
            break
    # Info commands
    elif cmd == "?" or cmd == "help":
        cmdProcessor.processHelp(args, force)
    elif cmd == "stats":
        cmdProcessor.processStats(args, force)
    # Database commands
    elif cmd == "add":
        cmdProcessor.processAdd(args, force)
    elif cmd == "remove":
        cmdProcessor.processRemove(args, force)
    elif cmd == "save":
        cmdProcessor.processSave(force)
    # Solve commands
    elif cmd == "match":
        cmdProcessor.processMatch(args, force)
    elif cmd == "hint":
        cmdProcessor.processHint(args, force)
    elif cmd == "reset":
        cmdProcessor.processReset(args, force)
    else:
        print("Error: Command not recognized")
print("Goodbye!")


