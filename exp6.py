# Knowledge Base (Facts)
facts = {
    "Runs": [
        ("Rajdhani", "Mumbai", "Delhi"),
        ("Shatabdi", "Delhi", "Bhopal"),
        ("Duronto", "Mumbai", "Kolkata")
    ],
    "Express": ["Rajdhani", "Shatabdi"],
    "Train": ["Rajdhani", "Shatabdi", "Duronto"]
}


# Function to check if a train runs between two cities
def Runs(train, source, destination):
    # Returns True if the tuple exists in facts
    return (train, source, destination) in facts["Runs"]


# Function to check if a train is express
def Express(train):
    return train in facts["Express"]


# Query 1: Which trains run from Mumbai?
print("Which trains run from Mumbai?")
for (train, src, dest) in facts["Runs"]:
    if src == "Mumbai":
        print(train)


# Query 2: Which train goes to Bhopal?
print("\nWhich train goes to Bhopal?")
for (train, src, dest) in facts["Runs"]:
    if dest == "Bhopal":
        print(train)


# Query 3: Is there an express train from Mumbai to Delhi?
print("\nIs there an express train from Mumbai to Delhi?")

# any() checks if at least one condition is True
result = any(
    Runs(t, "Mumbai", "Delhi") and Express(t)
    for t in facts["Train"]
)

print(result)




#output
# Which trains run from Mumbai?
# Rajdhani
# Duronto

# Which train goes to Bhopal?
# Shatabdi

# Is there an express train from Mumbai to Delhi?
# True

# Aim: To implement First Order Logic.
# Title: To implement First Order Logic using Python

# Theory:
# First Order Logic in Artificial Intelligence is a technique used for knowledge representation. It is an
# extension of propositional logic and unlike propositional logic; it is sufficiently expressive in representing
# any natural language construct. First Order Logic in AI is also known as Predicate Logic or First Order
# Predicate Logic. It is a robust technique to represent objects as well as their relationships. Unlike
# propositional logic, First Order Logic in Artificial Intelligence doesn&#39;t only include facts but also different
# other entities as listed below.
# Objects:
# Objects can denote any real-world entity or any variable. E.g., A, B, colours, theories, circles etc.
# Relations:
# Relations represent the links between different objects. Relations can be unary (relations defined for a
# single term) and n-ary (relations defined for n terms). E.g., blue, round (unary); friends, siblings (binary);
# etc.
# Functions:
# Functions map their input object to the output object using their underlying relation. Eg: father_of
# (), mother_of () etc.
# In the subsequent sections, we present the parts of First Order Logic in AI, i.e., the syntax and the
# semantics.
# Parts of First Order Logic
# First-order logic in Artificial Intelligence comprises two main components, which are as follows.
# Syntax:
# Syntax represents the rules to write expressions in First Order Logic in Artificial Intelligence.
# Semantics:
# Semantics refers to the techniques that we use to evaluate an expression of First Order Logic in AI.
# These techniques use various known relations and facts of the respective environment to deduce the
# boolean value of the given First Order Logic expression.
