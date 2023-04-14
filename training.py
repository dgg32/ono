examples = """
# はっきり; What does はっきり mean?
MATCH (w:Word {word: "はっきり"})
RETURN w.explanation AS result

# Give me the synonyms of きっちり; Similar words of きっちり? Other words similar to きっちり?
MATCH (w:Word {word: "きっちり"}) <-[r:SIMILAR_TO]-(o:Word)
RETURN o.word AS result LIMIT 10

# How to pronounce うろうろ?; What is the romaji of うろうろ?
MATCH (w:Word {word: "うろうろ"})
RETURN w.romaji AS result

# Examples of the word うろうろ?; Show me how to use うろうろ
MATCH (w:Word {word: "うろうろ"})
RETURN w.examples AS result

# Show me the words that belong to the JLPT N1; Words in JLPT N1?
MATCH (w:Word)
WHERE w.properties CONTAINS "JLPT N1"
RETURN w.word AS result LIMIT 10

# Show me the words that belong to the JLPT N2; Words in JLPT N2?
MATCH (w:Word)
WHERE w.properties CONTAINS "JLPT N2"
RETURN w.word AS result LIMIT 10

#Which words mean "carelessly"? Give me words that have the meaning "carelessly".; What are the onomatopoeia that mean "carelessly"?
MATCH (w:Word)
WHERE w.explanation CONTAINS "carelessly"
RETURN w.word AS result LIMIT 10
"""