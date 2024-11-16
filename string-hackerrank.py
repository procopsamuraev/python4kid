def main(text):
    list = []
    for word in text.split(" "):
        if word.endswith("ing"):
            list.append(word.removesuffix("ing")[:7])
        elif word.endswith("ly"):
            list.append(word.removesuffix("ly")[:7])
        elif word.endswith("re"):
            list.append(word.removesuffix("re")[:7])
        else:
            list.append(word)

    # return list
    print(' '.join(list))

if __name__ == "__main__":
    main("Working lecture wwwwwwworking ssssssssssssly")