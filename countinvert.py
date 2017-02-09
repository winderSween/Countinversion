# Tom Wu and Shengwei Huang
# Starter Code for Counting Inversions, Q1 HW4
# CS 2123, The University of Tulsa

from collections import deque
import itertools

def mergeandcount(lft,rgt):
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """

    sorted_combined_list = []
    number_of_inversions = 0
    i = 0
    j = 0
    while (i < len(lft) and j < len(rgt)):
		if lft[i] > rgt[j]:
			sorted_combined_list.append(rgt[j])
			number_of_inversions += len(lft[i:])
			print rgt[j], "conflicts with", lft[i:]
			j += 1
		else:
			sorted_combined_list.append(lft[i])
			i += 1

    for i in lft[i:]:
        sorted_combined_list.append(i)
    for j in rgt[j:]:
        sorted_combined_list.append(j)
    return (number_of_inversions, sorted_combined_list)

def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
  

    # print "leftside", leftside
    # print "rightside", rightside
    # print "whole seq", seqSorted
    leftside = seq[:len(seq)/2]
    rightside = seq[len(seq)/2:]
    if len(seq) <= 1:
    	return (0, seq)
    else:
        (ra,A)= sortandcount(leftside)
        (rb,B) = sortandcount(rightside)
        (rab,L)=mergeandcount(A,B)
    return (ra+rb+rab,L)


    return (global_inversions, seqSorted[1])

    

if __name__ =="__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (5,"Cake: I Will Survive"),
             (6,"Aretha Franklin: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs2 = [(3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (8,"Coldplay: Clocks"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs3 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (10,"Garth Brooks: Friends in Low Places"),
             (9,"Nickelback: Gotta be Somebody")]
    print seq1
    print "# Inversions: %i\n" %sortandcount(seq1)[0]
    print seq2
    print "# Inversions: %i\n" %sortandcount(seq2)[0]
    print seq3
    print "# Inversions: %i\n" %sortandcount(seq3)[0]
    print songs1
    print "# Inversions: %i\n" %sortandcount(songs1)[0]
    print songs2
    print "# Inversions: %i\n" %sortandcount(songs2)[0]
    print songs3
    print "# Inversions: %i\n" %sortandcount(songs3)[0]
