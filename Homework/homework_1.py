"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dna_dictionary = {'C':'G', 'T':'A', 'G':'C', 'A':'T'}

    result = ""
    for str in dna:
        result += dna_dictionary[str]
    return result

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    result =""
    result += s[0:start]
    result +=s[stop+1:len(s)]
    return result

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    result_list = []
    for i in range(len(s)-k+1):
        result_list.append(s[i:i+k])
    return result_list

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    result_set = set()
    for i in range(len(s)-k+1):
        result_set.add(s[i:i+k])
    return result_set

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    result_dict = {}
    for i in range(len(s)-k+1):
        if s[i:i+k] in result_dict:
            result_dict[s[i:i+k]] +=1
        else:
            result_dict[s[i:i+k]] = 1
    return result_dict

# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name,'r') as infile:
        lines = infile.readlines()
        line = lines[0:10]
        for text in line:
            print(text)
    return

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name,'r') as infile:
        lines = infile.readlines()
        line = lines[len(lines)-11:len(lines)]
        for text in line:
            print(text)
    return

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open(file_name,'r') as infile:
        lines = infile.readlines()
        for i in range(len(lines)):
            if i%2 != 0:
                print(lines[i])
    return

import csv
def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    result = []
    with open(file_name, newline='') as csv_file:
        reader =csv.reader(csv_file)
        for row in reader:
            result.append(row)
    return result

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    result = []
    with open(file_name, newline='') as csv_file:
        reader =csv.reader(csv_file)
        for row in reader:
            result.append(row[column])
    return result

def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    result = []
    with open(file_name,'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        seqs.remove('')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                result.append(sequence)
            except:
                print("Seqeunce not found")
    return result

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    result = []
    with open(file_name,'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        seqs.remove('')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                result.append(header)
            except:
                print("Header not found")
    return result

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    result = {}
    with open(file_name,'r') as infile:
        text = infile.read()
        seqs = text.split('>')
        seqs.remove('')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header = x[0]
                sequence = x[1].replace('\n', '')
                result[header] = sequence
            except:
                print("Header not found")
    return result

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    if not new_name:
        name = file_name.split('.')
        new_name = name[0]+".fasta"
    header = []
    sequence = []
    with open(file_name,'r') as infile:
        text = infile.read()
        seqs = text.split('@')
        seqs.remove('')
        for seq in seqs:
            try:
                x = seq.split('\n', 1)
                header.append(">"+x[0])
                s = x[1].split('+')
                print(s)
                sequence.append(s[0].replace('\n',''))
            except:
                print("No entry")
    with open(new_name,'w') as outfile:
        for i in range(len(header)):
            outfile.write(header[i]+"\n"+sequence[i]+"\n")

    return

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    dna_dictionary = {'C':'G', 'T':'A', 'G':'C', 'A':'T'}

    result = ""
    for str in dna:
        result += dna_dictionary[str]
    return result[::-1]

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    result = dna.replace('T','U')
    return result

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    result = ""
    for i in range(0,len(rna),3):
        result +=RNA_CODON_TABLE[rna[i:i+3]]
    protein = result.replace('*','')
    return protein

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    frames = []
    rev_comp_dna = reverse_complement(dna)
    rf_1 = ""
    rf_2 = dna[0:1]
    rf_3 = dna[0:2]
    rf_4 = ""
    rf_5 = rev_comp_dna[0:1]
    rf_6 = rev_comp_dna[0:2]
    for i in range(0,len(dna),3):
        rf_1 += " "+dna[i:i+3]
        rf_2 += " "+dna[i+1:i+4]
        rf_3 += " "+dna[i+2:i+5]
        rf_4 += " "+rev_comp_dna[i:i+3]
        rf_5 += " "+rev_comp_dna[i+1:i+4]
        rf_6 += " "+rev_comp_dna[i+2:i+5]
    frames.extend([rf_1,rf_2,rf_3,rf_4,rf_5,rf_6])
    return frames


