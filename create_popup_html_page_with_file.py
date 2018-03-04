import random
import copy


def main():
    filename = input('Filename: ')
    try:
        print('Begin...')
        with open(filename, 'r') as f:
            list_res = [word.strip().replace('"', "'") for line in f for word in line.split(' ')]

        id_res = ['a' + str(i).zfill(8) + '()' for i in range(len(list_res))]
        random.shuffle(id_res)

        res = [(id_res[i], list_res[i]) for i in range(len(list_res))]

    except FileNotFoundError:
        print('File not found !')
        return

    with open('public.html', 'w') as f:
        f.write('<script>\n')
        for el in res:
            f.write(el[0] + '\n')

        random.shuffle(res)
        for el in res:
            f.write('function ' + el[0] + '{alert("' + el[1] + '");}\n')
        f.write('</script>')
    print('Done !')
main()
