num_books,time_to_read = map(int, input().split())
time_per_book = list(map(int, input().split()))

i = 0
j = 0
remaining_time = time_to_read
books_read = 0
while i < num_books and j < num_books:
    while j < num_books:
        remaining_time -= time_per_book[j]
        j+=1
        if remaining_time < 0:
          j-=1
          remaining_time+=time_per_book[j]
          break
    
    books_read = max([books_read, j-i])
    remaining_time += time_per_book[i]
    i+=1

print(books_read)