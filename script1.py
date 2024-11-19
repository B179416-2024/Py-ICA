#!/usr/bin/python3

# Script: BPSM Python ICA
# Objective:
# Version:
# Last Update:
# Updated: 17-NOV-2024
# Created: 17-NOV-2024
# Author:


# Loading libraries
import sys, shutil, subprocess
import pandas as pd
import numpy as np

# Task 1: User Input Collection
# Objective: collect input from user to define protein family and taxonomic group.

def get_user_input():
    print("Welcome to my Ultimate Bioinformatics Tool!")
    print("This script will take a protein family and the taxonomic group you specify, and output some magical report at the end. [If you see this, means I haven't completed it yet].")

    #Get lowercase input
    protein_family = input("\nEnter the protein family:\n").lower()
    taxonomic_group = input("\nEnter the taxonomic group:\n").lower()

    #Remove any trailing spaces 
    if protein_family[-1] == " ":
        protein_family = protein_family[:-1]
    if taxonomic_group[-1] == " ":
        taxonomic_group = taxonomic_group[:-1]

    #If any is empty, raise an error!!!
    if not protein_family or not taxonomic_group:
        raise ValueError("I really can't to much if you don't give me information for both!!")

    #Inform the user of parameters selected
    print("\nYou have selected the protein family:",protein_family,", and the taxonomic_group:",taxonomic_group,".")
    
    #Get confirmation from the user
    confirm = input("\nAre you happy to proceed with those parameters (y/n)?\n")

    if confirm != "y":
        print("You have not selected 'y', so we are exiting the program...\nHope to see you again!")
        return
    
    #Finish the function and get the important info if all went well.
    return protein_family, taxonomic_group
    

def get_database(protein_family = "glucose-6-phosphatase", taxonomic_group = "aves"):

    entries = subprocess.check_output(["esearch -db protein -query '"+protein_family+" [PROT] AND "+taxonomic_group+" [ORGN]' | efetch -format fasta"], shell = True).decode("utf-8")

    sequences = entries.split("\n")

        #Check the search isn't empty or there are >1000!
    count = entries.count(">")
    if count == 0:
        raise ValueError("The search was empty... either your input had some error, or you are researching something never-seen-before!")
    
    elif count > 1000:
        print("My friend, that's a popular one! More than 1,000 sequences were found.")
        confirm = input("I recommend refining your interests. Do you still want to proceed? (y/n)")
        if confirm != "y":
            print("You have not selected 'y', so we are exiting the program...\nHope to see you again!")
            return
    database = open("sequences.txt","w")
    database.write(entries)
    database.close()

    return count

def mult_alignment(file_name="sequences.txt"):
    
    #Below is not needed. I originally coded it to format the input for the Python package 'clustalo', which isn't loaded.
    #sequences = open(file_name).read()

    #seq = sequences.split(">")

    #seq_dict = {}
    #for i in seq:
    #    end_name = i.find("]") + 1
    #    name = i[:end_name]
    #    sequence = i[end_name:].replace("\n","")
        
    #    seq_dict[name] = sequence

    #So I'm using bash clustalo instead
    subprocess.call(["clustalo -i "+file_name+" -o alignment.out -v"], shell=True)
    subprocess.call("plotcon -sequences alignment.out -graph png -winsize 5", shell=True)
    subprocess.call("infoalign -sequence alignment.out -outfile 'alignment.info'", shell=True)

    return "Alignment done!"
