import urls

words = urls.confi_read.extract_variables(urls.CONFI)

links_to_files = urls.find_files.find_html_files(urls.RAWS)

old_lists = {}
new_lists = {}

for x in links_to_files:

    lines = []
    with open(urls.RAWS+ "/" + x, 'r') as file: lines = file.readlines()

    old_lists[x] = lines

for x in old_lists.keys():new_lists[x] = urls.replacer.TextReplacer(words["link_word"]).replace(old_lists[x])

for x in new_lists.keys():

    with open(urls.NEWS+ "/" + x, 'w') as file: file.writelines(new_lists[x])

print("job done")