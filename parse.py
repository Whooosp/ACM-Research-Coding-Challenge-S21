# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO


def parse(filename):
    # get all sequence records for the specified genbank file
    recs = [rec for rec in SeqIO.parse(filename, "genbank")]

    for rec in recs:
        feats = [feat for feat in rec.features if feat.type == "CDS"]
        return feats


def get_source(filename):
    recs = [rec for rec in SeqIO.parse(filename, "genbank")]

    for rec in recs:
        source = next(feat for feat in rec.features if feat.type == "source")
        return source
