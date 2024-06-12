clothes = [int(x) for x in input().split()]
rag_space = int(input())

rag_count = 1
current_rag_space = rag_space

while clothes:
    cloth = clothes.pop()

    if current_rag_space >= cloth:
        current_rag_space -= cloth

    else:
        rag_count += 1
        current_rag_space = rag_space - cloth


print(rag_count)