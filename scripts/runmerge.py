import os

os.system('mdmerge -o docs/merged.md ${PWD}/docs/By-approach/asking-questionsorig.md ${PWD}/docs/By-approach/communicatingorig.md ${PWD}/docs/By-approach/files.md ${PWD}/docs/By-approach/liking-posts ${PWD}/docs/By-approach/voice.md ${PWD}/docs/By-approach/working-out-loud.md ${PWD}/docs/By-service/onenoteorig.md ${PWD}/docs/By-service/outlookorig.md ${PWD}/docs/By-service/plannerorig.md ${PWD}/docs/By-service/teamsorig.md')
os.system('mdmerge -o docs/By-service/onenote.md "${PWD}/content/OneNote.md" "${PWD}/content/OneNote-Avoid local.md"  "${PWD}/content/OneNote-Avoid too many.md" "${PWD}/content/OneNote-Create sections for each meeting.md" "${PWD}/content/OneNote-Name pages effectively.md" "${PWD}/content/OneNote-One per project.md" "${PWD}/content/OneNote-Share your notes.md"')
os.system('mdmerge -o docs/By-service/outlook.md "${PWD}/content/Outlook.md" "${PWD}/content/Outlook-Email-At mentions.md" "${PWD}/content/Outlook-Email-CC people.md" "${PWD}/content/Outlook-Email-People in to line.md" "${PWD}/content/Outlook-Email-Read receipts.md" "${PWD}/content/Outlook-Email-Signatures.md" "${PWD}/content/Outlook-Meetings-Agenda.md" "${PWD}/content/Outlook-Meetings-Findtime.md" "${PWD}/content/Outlook-Meetings-Scheduling assistant.md" "${PWD}/content/Outlook-OOO-Dates and contacts.md" "${PWD}/content/Outlook-OOO-Do not leave OOO on.md" "${PWD}/content/Outlook-OOO-Expectations.md"')
os.system('mdmerge -o docs/By-service/planner.md "${PWD}/content/Planner.md" "${PWD}/content/Planner-Assignments.md" "${PWD}/content/Planner-Dates-Filter.md" "${PWD}/content/Planner-Dates-Flagged tasks.md" "${PWD}/content/Planner-Dates-Scheduled.md" "${PWD}/content/Planner-Dates-Set dates.md" "${PWD}/content/Planner-Labels-Categorise.md" "${PWD}/content/Planner-Labels-Filter.md" "${PWD}/content/Planner-Labels-Group tasks by label.md" "${PWD}/content/Planner-Use of buckets.md"')

dirFiles = os.listdir('.')
    dirFiles.sort()
    for foundFile in dirFiles:
        print(foundFile)