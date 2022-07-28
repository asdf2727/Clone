import CmdProcessor as cp

print("Welcome to Wordle helper!")
cmdProcessor = cp.CmdProcessor()
while True:
    line = input("> ").lower()
    args = line.split()
    cmd = args[0]
    args.pop(0)
    if cmd == "quit" or cmd == "exit":
        if cmdProcessor.processExit():
            break
    # Info commands
    elif cmd == "?" or cmd == "help":
        cmdProcessor.processHelp(args)
    elif cmd == "stats":
        cmdProcessor.processStats(args)
    # Database commands
    elif cmd == "add":
        cmdProcessor.processAdd(args)
    elif cmd == "remove":
        cmdProcessor.processRemove(args)
    elif cmd == "save":
        cmdProcessor.processSave()
    # Solve commands
    elif cmd == "match":
        cmdProcessor.processMatch(args)
    elif cmd == "hint":
        cmdProcessor.processHint(args)
    elif cmd == "reset":
        cmdProcessor.processReset(args)
    elif cmd != "":
        print("Error: Command not recognized")
print("Goodbye!")


