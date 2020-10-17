import os

def runMerge(folderPath):
    dirFiles = os.listdir('./' + folderPath)
    fileList = ""
    for foundFile in dirFiles:
        fileList += "\"${PWD}/" + folderPath + "/" + foundFile + "\" "
    print(fileList)

    os.system('mdmerge -o docs/By-approach/Asking-questions.md ' + fileList)
    return

os.system('mdmerge -o docs/merged.md ${PWD}/docs/By-approach/asking-questionsorig.md ${PWD}/docs/By-approach/communicatingorig.md ${PWD}/docs/By-approach/files.md ${PWD}/docs/By-approach/liking-posts ${PWD}/docs/By-approach/voice.md ${PWD}/docs/By-approach/working-out-loud.md ${PWD}/docs/By-service/onenoteorig.md ${PWD}/docs/By-service/outlookorig.md ${PWD}/docs/By-service/plannerorig.md ${PWD}/docs/By-service/teamsorig.md')

runMerge('content/By approach/Asking questions')
runMerge('content/By approach/Communicating')
runMerge('content/By service/OneNote')
runMerge('content/By service/Outlook')
runMerge('content/By service/Planner')
runMerge('content/By service/Teams')