"""_summary_:
    Debug server starting script.
"""

if __name__ == "__main__":
    from . import root
    root.run(host="0.0.0.0", port=5000)