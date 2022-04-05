import csv
from collections import Counter
from itertools import groupby
while True:
    filename = input("Enter the filename of an Apple Music or iTunes playlist data file. ")
    
    try:
        
        with open(filename, encoding = 'utf-16') as f:
        
            csvreader = csv.reader(f, delimiter ='\t')
            header = next(csvreader)

            rows = []
            years = []
            songs_time = []
            songs_genre = []
            songs_played = []
            song_count = 0
            for row in csvreader:
                rows.append(row)
                song_count+=1

            for i in rows:
                years.append(i[16]) 
                songs_time.append(i[0])
                songs_time.append(i[1])
                songs_time.append(i[11])
                songs_genre.append(i[9])   
                songs_genre.append(i[0])
                songs_genre.append(i[1])
                songs_genre.append(i[11])
                songs_played.append(i[25])

                # element 16 = year
                # element 0 = name
                # element 1 = album
                # element 11 = time
                # element 9 = genre
                # element 25 = plays

            yearsres = Counter(years)

            z = iter(songs_time)          
            songs_time = list(zip(z,z,z)) # group songs by every 3 elements
        
            sorted_songs_time = sorted(songs_time, key = lambda x: int('0' + x[2]))
            
            shortest_song = sorted_songs_time[0]

            longest_song = sorted_songs_time[-1]
            

            x = iter(songs_genre)          
            songs_genre = list(zip(x,x,x,x)) # group songs by every 4 elements
        
            sorted_songs_genre = sorted(songs_genre, key = lambda x: (x[0], int('0' + x[3])))

            grouped_genre = groupby(sorted_songs_genre, key = lambda x : (x[0]))

            grouped_genre2 = groupby(sorted_songs_genre, key = lambda x : (x[0]))

            minvalues = [(k, min(g, key=lambda x: int('0' + x[3]))) for k, g in grouped_genre]

            maxvalues = [(k, max(g, key=lambda x: int('0' + x[3]))) for k, g in grouped_genre2]
            

            genre_count = Counter(i[0] for i in songs_genre)
 
            
            played = sum(1 for i in songs_played if i)
            not_played = sum(1 for i in songs_played if not i)
            
    except FileNotFoundError:
        print("Not a valid filename.")
        continue

    def main():
        
        print("\nTotal number of songs in the playlist:",song_count)

        print("\nNumber of songs each year:")

        for k, v in yearsres.items():
            print(k,':',v)

        print("\nLongest song:",longest_song)

        print("\nShortest song:",shortest_song)

        print("\nAmount of songs per genre:")

        for k, v in genre_count.items():
            print(k,':',v)

        print("\nLongest songs by genre:")

        for x in maxvalues:
            print(x[1])

        print("\nShortest songs by genre:")
        for x in minvalues:
            print(x[1])

        print("\nNumber of songs that have been played:",played)

        print("\nNumber of songs that have not been played:",not_played)

    main()