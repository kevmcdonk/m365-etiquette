import os

os.system('mdmerge -o docs/merged.md ${PWD}/docs/By-approach/asking-questionsorig.md ${PWD}/docs/By-approach/communicatingorig.md ${PWD}/docs/By-approach/files.md ${PWD}/docs/By-approach/liking-posts ${PWD}/docs/By-approach/voice.md ${PWD}/docs/By-approach/working-out-loud.md ${PWD}/docs/By-service/onenoteorig.md ${PWD}/docs/By-service/outlookorig.md ${PWD}/docs/By-service/plannerorig.md ${PWD}/docs/By-service/teamsorig.md')

dirFiles = os.listdir('./content/By approach/Asking questions')
fileList = ""
for foundFile in dirFiles:
    fileList += foundFile + " "
print(fileList)

os.system('mdmerge -o docs/By-approach/Asking-questions.md ' + fileList)