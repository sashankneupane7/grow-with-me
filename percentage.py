with open("README.md", "r", encoding="utf-8") as f:
    textt = f.read()
    completed = textt.count("[X]")
    incomplete = textt.count("[ ]")
    percent = str(int(completed/(completed+incomplete)*100))+" % has been learnt from this list."
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines[3] = "## " +percent+"\n"
    lines[4] = "<b>`"+ str(completed) +"`</b>"+" completed || "+ "<b>`"+str(incomplete)+"`</b>"+" remaining"+"\n"
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)