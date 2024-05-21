# Method for the DataAnnotation coding challenge 1, to get the last word in each line of triangle.

def decode(message_file):
    # Read the file and split each line into a separate list element
    txt = open(message_file, 'r').read()
    txt = txt.split('\n')
    #Sort the text by the numbers
    txt = [ [int(x.split(' ')[0]), x.split(' ')[1]] for x in txt]
    txt.sort()
    print('SORTED')
    print(txt)
    # Initialize variables
    out = []
    i = 0
    # Loop through list getting the last element of each line until
    # the end of the list is reached.
    while True:
        i += 1
        tri = int((i * (i + 1)) / 2)
        if tri > len(txt):
            break
        last = txt[tri-1][1]
        out = out + [last]
    
    #Format the output by removing numbers:
    out = ' '.join(out)
    return out
    

out = decode('input2.txt')
print('OUTPUT:', out)