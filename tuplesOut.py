def tuplesOut(dictionary):
    new_arr = []
    for key, data in dictionary.items():
        new_arr.append((key, data))
    print new_arr

tuplesOut({
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
})