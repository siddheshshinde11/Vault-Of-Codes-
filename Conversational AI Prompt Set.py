import random
import json
import os
from datetime import datetime

class ConversationalAI:
    def _init_(self, name="Assistant"):
        self.name = name
        self.conversation_history = []
        self.user_profile = {}
        self.mode = "general"  # Modes: general, faq, fun, knowledge
        self.faq_data = self._load_faq_data()
        self.knowledge_base = self._load_knowledge_base()
        
        # Prompt templates for different conversation flows
        self.prompts = {
            "greeting": [
                f"Hello! I'm {self.name}. How can I assist you today?",
                f"Hi there! I'm {self.name}. What would you like to talk about?",
                f"Greetings! I'm {self.name}. I can help with questions, have fun conversations, or discuss various topics. What interests you?"
            ],
            "faq_mode": [
                "I see you have a question. Let me find the answer for you.",
                "That's a good question. Here's what I know:",
                "I'd be happy to answer that question."
            ],
            "fun_mode": [
                "Let's have some fun! What would you like to talk about?",
                "I'm in a playful mood! What's on your mind?",
                "Fun conversations are my specialty! What shall we discuss?"
            ],
            "knowledge_mode": [
                "I'd be happy to discuss this topic in depth.",
                "That's an interesting subject. Let me share what I know.",
                "I enjoy knowledge-based discussions. Here's some information on that:"
            ],
            "clarification": [
                "Could you provide more details about that?",
                "I'm not sure I understand. Can you elaborate?",
                "To better assist you, could you explain a bit more?"
            ],
            "context_recall": [
                "Earlier you mentioned {previous_topic}. Would you like to continue that discussion?",
                "Going back to {previous_topic} that you brought up earlier...",
                "Relating to our previous conversation about {previous_topic}..."
            ],
            "farewell": [
                "It was great chatting with you! Feel free to return if you have more questions.",
                "I enjoyed our conversation! Come back anytime.",
                "Thanks for the chat! Have a wonderful day!"
            ]
        }
    
    def _load_faq_data(self):
        # In a real implementation, this would load from a file or database
        return {
            "what can you do": "I can answer questions, have fun conversations, and discuss various topics with you.",
            "how do you work": "I'm a conversational AI designed to maintain context and provide engaging responses.",
            "who created you": "I was created as part of a programming project to demonstrate conversational AI capabilities."
        }
    
    def _load_knowledge_base(self):
        # In a real implementation, this would load from a file or database
        return {
            "artificial intelligence": "Artificial Intelligence (AI) refers to systems designed to perform tasks that typically require human intelligence.",
            "machine learning": "Machine Learning is a subset of AI that enables systems to learn from data and improve over time without explicit programming.",
            "natural language processing": "Natural Language Processing (NLP) is a field of AI focused on enabling computers to understand and generate human language."
        }
    
    def detect_intent(self, user_input):
        """Determine the user's intent from their input"""
        user_input = user_input.lower()
        
        # Check if it's a FAQ
        for question in self.faq_data.keys():
            if question in user_input:
                self.mode = "faq"
                return {"type": "faq", "question": question}
        
        # Check if it's a knowledge request
        for topic in self.knowledge_base.keys():
            if topic in user_input:
                self.mode = "knowledge"
                return {"type": "knowledge", "topic": topic}
        
        # Check if it's a fun conversation request
        fun_keywords = ["joke", "fun", "play", "game", "entertain"]
        if any(keyword in user_input for keyword in fun_keywords):
            self.mode = "fun"
            return {"type": "fun"}
        
        # Check for greetings
        greetings = ["hello", "hi", "hey", "greetings"]
        if any(greeting in user_input for greeting in greetings):
            return {"type": "greeting"}
        
        # Check for farewells
        farewells = ["bye", "goodbye", "see you", "farewell"]
        if any(farewell in user_input for farewell in farewells):
            return {"type": "farewell"}
        
        # Default to general conversation
        self.mode = "general"
        return {"type": "general", "input": user_input}
    
    def generate_response(self, user_input):
        """Generate a response based on user input and conversation history"""
        # Add user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input, "timestamp": datetime.now().isoformat()})
        
        # Detect intent
        intent = self.detect_intent(user_input)
        response = ""
        
        # Generate response based on intent
        if intent["type"] == "greeting":
            response = random.choice(self.prompts["greeting"])
        
        elif intent["type"] == "farewell":
            response = random.choice(self.prompts["farewell"])
        
        elif intent["type"] == "faq":
            prompt = random.choice(self.prompts["faq_mode"])
            answer = self.faq_data[intent["question"]]
            response = f"{prompt} {answer}"
        
        elif intent["type"] == "knowledge":
            prompt = random.choice(self.prompts["knowledge_mode"])
            info = self.knowledge_base[intent["topic"]]
            response = f"{prompt} {info}"
        
        elif intent["type"] == "fun":
            response = random.choice(self.prompts["fun_mode"])
            # In a real implementation, this would include jokes, games, etc.
            response += " How about I tell you a joke? Why don't scientists trust atoms? Because they make up everything!"
        
        else:  # general conversation
            # Check if we can use context from previous conversation
            if len(self.conversation_history) > 2:
                previous_topics = self._extract_topics_from_history()
                if previous_topics:
                    previous_topic = random.choice(previous_topics)
                    context_prompt = random.choice(self.prompts["context_recall"])
                    response = context_prompt.format(previous_topic=previous_topic)
                else:
                    # If no clear context, ask for clarification
                    response = random.choice(self.prompts["clarification"])
            else:
                # Not enough history for context, use clarification
                response = random.choice(self.prompts["clarification"])
        
        # Add response to conversation history
        self.conversation_history.append({"role": "assistant", "content": response, "timestamp": datetime.now().isoformat()})
        
        return response
    
    def _extract_topics_from_history(self):
        """Extract potential topics from conversation history"""
        # In a real implementation, this would use NLP to extract topics
        # For this example, we'll use a simple approach
        topics = []
        for entry in self.conversation_history[-5:]:  # Look at last 5 entries
            if entry["role"] == "user":
                # Extract potential topics (words longer than 4 characters)
                words = entry["content"].lower().split()
                topics.extend([word for word in words if len(word) > 4])
        
        return topics[:3]  # Return up to 3 potential topics
    
    def update_user_profile(self, key, value):
        """Update user profile with new information"""
        self.user_profile[key] = value
    
    def save_conversation(self, filename="conversation_history.json"):
        """Save the conversation history to a file"""
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def load_conversation(self, filename="conversation_history.json"):
        """Load conversation history from a file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.conversation_history = json.load(f)


# Example usage demonstrating the flow of prompts
def simulate_conversation():
    chatbot = ConversationalAI(name="Chatty")
    
    # Prompt 1: Greeting
    user_input = "Hello there!"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Prompt 2: FAQ question
    user_input = "What can you do?"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Prompt 3: Knowledge-based question
    user_input = "Tell me about artificial intelligence"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Prompt 4: Fun conversation
    user_input = "Let's have some fun"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Prompt 5: General conversation with context retention
    user_input = "That's interesting"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Prompt 6: Farewell
    user_input = "Goodbye for now"
    print(f"User: {user_input}")
    response = chatbot.generate_response(user_input)
    print(f"{chatbot.name}: {response}\n")
    
    # Save the conversation history
    chatbot.save_conversation()


if _name_ == "_main_":
    simulate_conversation()
