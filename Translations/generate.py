import os

languages = ["German", "French", "Italian", "Spanish", "Russian", "Serbian", "Hebrew", "Dutch", "Turkish"]; # Exclude English because thats the default language

# Filter all Template Files
templateFiles = [];
for file in os.listdir("native"):
    if file.endswith(".lang"):
        templateFiles.append(file);

if len(templateFiles) == 0:
    print("Please add templates into the native folder");
    exit();

print("Generating...");

for templateFile in templateFiles:
    templateName = templateFile.split("_")[0]
    templateReader = open("native/"+templateFile, "r");
    templateLines = templateReader.readlines();
    templateReader.close();

    for language in languages:
        fileName = templateName+"_"+language+".lang";

        print("["+fileName+"] Syncing...");

        # Retrieve all set phrases
        existingPhrases = [];
        phrases = {};

        try:
            fileReader = open(fileName, "r+")
            for line in fileReader.readlines():
                split = line.split(": ");
                existingPhrases.append(split[0].replace("#", ""));

                if "#" in line:
                    continue;

                phrases[split[0]] = split[1];

            fileReader.close();
        except IOError:
            pass;

        fileWriter = open(fileName, "w+");

        for line in templateLines:
            split = line.split(": ");

            if len(split) != 2:
                continue;

            phraseName = split[0];
            value = split[1];

            if phraseName in phrases:
                value = phrases[phraseName];
                fileWriter.write(phraseName+": "+value);
            else:
                if (phraseName in existingPhrases) == False:
                    print("["+fileName+"] Created Phrase '"+phraseName+"'");

                fileWriter.write("#"+phraseName+": "+value);

        fileWriter.close();

print("Done!");
