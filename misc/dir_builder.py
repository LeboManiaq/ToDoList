contents = ["something about docs", "something about reports", "something about presentations"]

filenames = ["doc.txt","reports.txt","presentation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)