def pagedisplay(input_csv_array, k):
    ids = [line.split(',')[0] for line in input_csv_array]
    hmap = {}
    pages = []
    start = 0

    for i, id in enumerate(ids):
        if id not in hmap or hmap[id] < start:
            hmap[id] = start
        if hmap[id] == len(pages):
            pages.append([])
        pages[hmap[id]].append(input_csv_array[i])
        hmap[id] += 1
        if len(pages[start]) == k:
            start += 1

    # if you need to print exact k lines in a page (i.e., tolerate some dup)
    # then have a third loop to print the page
    for page in pages:
        print('---- page ----')
        for line in page:
            print(line)


def my_pagedisplay(input_csv_array, k):
    ids = [line.split(',')[0] for line in input_csv_array]
    start = dict()
    pages = []

    now = 0
    for i, idx in enumerate(ids):
        if idx not in start or start[idx] < now:
            start[idx] = now
        if start[idx] == len(pages):
            pages.append([])
        pages[start[idx]].append(input_csv_array[i])
        start[idx] += 1

        if len(pages[now]) == k:
            now += 1

    for page in pages:
        print('---- page ----')
        for line in page:
            print(line)


input_csv_array = [
    "1,28,300.1,SanFrancisco",
    "4,5,209.1,SanFrancisco",
    "20,7,208.1,SanFrancisco",
    "23,8,207.1,SanFrancisco",
    "16,10,206.1,Oakland",
    "1,16,205.1,SanFrancisco",
    "6,29,204.1,SanFrancisco",
    "7,20,203.1,SanFrancisco",
    "8,21,202.1,SanFrancisco",
    "2,18,201.1,SanFrancisco",
    "2,30,200.1,SanFrancisco",
    "15,27,109.1,Oakland",
    "10,13,108.1,Oakland",
    "11,26,107.1,Oakland",
    "12,9,106.1,Oakland",
    "13,1,105.1,Oakland",
    "22,17,104.1,Oakland",
    "1,2,103.1,Oakland",
    "28,24,102.1,Oakland",
    "18,14,11.1,SanJose",
    "6,25,10.1,Oakland",
    "19,15,9.1,SanJose",
    "3,19,8.1,SanJose",
    "3,11,7.1,Oakland",
    "27,12,6.1,Oakland",
    "1,3,5.1,Oakland",
    "25,4,4.1,SanJose",
    "5,6,3.1,SanJose",
    "29,22,2.1,SanJose",
    "30,23,1.1,SanJose"
]

input_csv_array2 = [
    "1,28,300.1,SanFrancisco",
    "29,22,2.1,SanJose",
    "28,22,2.1,SanJose",
    "29,22,2.1,SanJose",
    "1,5,209.1,SanFrancisco",
    "1,7,208.1,SanFrancisco"
]

input_csv_array3 = [
    "1,28,300.1,SanFrancisco",
    "1,5,209.1,SanFrancisco",
    "1,7,208.1,SanFrancisco",
    "28,22,2.1,SanJose",
    "29,22,2.1,SanJose",
]

print("\ninput_csv_array")
pagedisplay(input_csv_array, 12)
print()
my_pagedisplay(input_csv_array, 12)
# print("\ninput_csv_array2")
# pagedisplay(input_csv_array2, 2)  # same id skip a page
# print("\ninput_csv_array3")
# pagedisplay(input_csv_array3, 2)  # page grows faster than ids
