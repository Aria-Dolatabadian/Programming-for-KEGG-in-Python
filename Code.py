# Show images inline
from IPython.display import Image
# Standard library packages
import io
import os
# Import Biopython modules to interact with KEGG
from Bio import SeqIO
from Bio.KEGG import REST
from Bio.KEGG.KGML import KGML_parser
from Bio.Graphics.KGML_vis import KGMLCanvas
# Import Pandas, so we can use dataframes
import pandas as pd
# A bit of code that will help us display the PDF output
def PDF(filename):
    return HTML('<iframe src=%s width=700 height=350></iframe>' % filename)
# Some code to return a Pandas dataframe, given tabular text
def to_df(result):
    return pd.read_table(io.StringIO(result), header=None)


# Perform the query
result = REST.kegg_info("kegg").read()
# Print the result
print(result)
# Specify the text file name
txt_file = "kegg_info_result.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")

# Convert result to dataframe
# NOTE: kegg_info() requests do not produce a suitable data format for dataframe representation
#to_df(result)

# Print information about the PATHWAY database
result = REST.kegg_info("pathway").read()
print(result)
# Specify the text file name
txt_file = "PATHWAY database.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Print information about Kitasatospora setae
result = REST.kegg_info("ksk").read()
print(result)
# Specify the text file name
txt_file = "Kitasatospora setae.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get all entries in the PATHWAY database as a dataframe
result = REST.kegg_list("pathway").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "PATHWAY database as a dataframe.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get all entries in the PATHWAY database for K. setae as a dataframe
result = REST.kegg_list("pathway", "ksk").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "PATHWAY database for K. setae as a dataframe.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get all genes from K. setae as a dataframe
result = REST.kegg_list("ksk").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "genes from K. setae as a dataframe.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Find a specific entry with a precise search term
result = REST.kegg_find("genes", "KSE_17560").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "Specific entry with a precise search term.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Find all shiga toxin genes
result = REST.kegg_find("genes", "shiga+toxin").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "shiga toxin genes.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Find all shiga toxin genes in eoi
result = REST.kegg_find("eoi", "shiga+toxin").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "shiga toxin genes in eoi.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Find all compounds with mass between 300 and 310 units
result = REST.kegg_find("compound", "300-310/mol_weight").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "compounds with mass between 300 and 310 units.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get the entry information for cpd:C00051
result = REST.kegg_get("cpd:C00051").read()
print(result)
# Specify the text file name
txt_file = "entry information for cpd:C00051.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Display molecular structure for cpd:C00051
result = REST.kegg_get("cpd:C00051", "image").read()
Image(result)
# Save the image to a file
with open("C00051.png", "wb") as f:
    f.write(result)
print("Image saved successfully.")
# Get entry information for KSE_17560
result = REST.kegg_get("ksk:KSE_17560").read()
print(result)
# Specify the text file name
txt_file = "information for KSE_17560.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get coding sequence for KSE_17560
result = REST.kegg_get("ksk:KSE_17560", "ntseq").read()
print(result)
# Specify the text file name
txt_file = "coding sequence for KSE_17560.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get protein sequence for KSE_17560
result = REST.kegg_get("ksk:KSE_17560", "aaseq").read()
print(result)
# Specify the text file name
txt_file = "protein sequence for KSE_17560.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get map of fatty-acid biosynthesis
result = REST.kegg_get("map00061", "image").read()
Image(result)
# Save the image to a file
with open("map of fatty-acid biosynthesis.png", "wb") as f:
    f.write(result)
print("Image saved successfully.")
# Get map of central metabolism
result = REST.kegg_get("map01100", "image").read()
Image(result)
# Save the image to a file
with open("map01100.png", "wb") as f:
    f.write(result)
print("Image saved successfully.")
# Get map of fatty-acid biosynthesis in Kitasatospora
result = REST.kegg_get("ksk00061", "image").read()
Image(result)
# Save the image to a file
with open("ksk00061.png", "wb") as f:
    f.write(result)
print("Image saved successfully.")
# Get map of central metabolism in Kitasatospora
result = REST.kegg_get("ksk01100", "image").read()
Image(result)
# Save the image to a file
with open("ksk01100.png", "wb") as f:
    f.write(result)
print("Image saved successfully.")
# Get data for fatty-acid biosynthesis in Kitasatospora
result = REST.kegg_get("ksk00061").read()
print(result)
# Specify the text file name
txt_file = "fatty-acid biosynthesis in Kitasatospora.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get genes involved with fatty-acid biosynthesis in Kitasatospora
result = REST.kegg_link("compound", "map00061").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "genes involved with fatty-acid biosynthesis in Kitasatospora.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get reactions involved with fatty-acid biosynthesis
result = REST.kegg_link("rn", "map00061").read()
to_df(result)
print(result)
# Specify the text file name
txt_file = "reactions involved with fatty-acid biosynthesis.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")
# Get reactions R00742
result = REST.kegg_get("R00742").read()
print(result)
# Specify the text file name
txt_file = "reactions R00742.txt"
# Write the result to a text file
with open(txt_file, mode="w") as file:
    file.write(result)
print(f"Results exported to {txt_file}")

