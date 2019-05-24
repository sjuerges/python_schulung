#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul
import re

# 1: Exakter Text
tx = "10.11.2000"
print(tx)
txneu = re.sub(r"^(\d{1,2})\.(\d{1,2})\.(\d{4})$", r"\3-\2-\1", tx)
print("1: ", txneu)
