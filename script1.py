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
    

