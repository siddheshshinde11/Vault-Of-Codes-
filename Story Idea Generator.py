import random
import json
from typing import List, Dict, Any, Optional

class StoryIdeaGenerator:
    def __init__(self):
        # Initialize with various story elements
        self.genres = [
            "Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", 
            "Adventure", "Historical Fiction", "Thriller", "Comedy", "Drama"
        ]
        
        self.character_types = [
            "Hero", "Villain", "Mentor", "Sidekick", "Love Interest", 
            "Anti-hero", "Trickster", "Guardian", "Outcast", "Innocent"
        ]
        
        self.plot_devices = [
            "Quest", "Mystery", "Revenge", "Escape", "Transformation", 
            "Sacrifice", "Discovery", "Rivalry", "Forbidden Love", "Redemption"
        ]
        
        self.settings = [
            "Medieval Kingdom", "Futuristic City", "Small Town", "Alien Planet", 
            "Post-apocalyptic World", "Ancient Civilization", "Haunted House", 
            "Underwater City", "Space Station", "Parallel Universe"
        ]
        
        self.themes = [
            "Betrayal", "Love", "Redemption", "Power", "Identity", 
            "Justice", "Freedom", "Survival", "Family", "Sacrifice"
        ]
        
        self.conflicts = [
            "Person vs. Person", "Person vs. Nature", "Person vs. Society", 
            "Person vs. Technology", "Person vs. Supernatural", "Person vs. Self", 
            "Person vs. Fate", "Person vs. Machine", "Person vs. God", "Person vs. Reality"
        ]
        
        # Store generated stories for potential sequels
        self.story_history: List[Dict[str, Any]] = []

    def generate_basic_idea(self) -> Dict[str, str]:
        """Generate a basic story idea with random elements"""
        return {
            "genre": random.choice(self.genres),
            "character_type": random.choice(self.character_types),
            "plot_device": random.choice(self.plot_devices),
            "setting": random.choice(self.settings),
            "theme": random.choice(self.themes),
            "conflict": random.choice(self.conflicts)
        }
    
    def create_prompt(self, elements: Dict[str, str]) -> str:
        """Create a story prompt based on the given elements"""
        prompts = [
            f"In a {elements['setting']}, a {elements['character_type'].lower()} faces {elements['conflict'].lower()} while pursuing {elements['plot_device'].lower()} in this {elements['genre'].lower()} tale about {elements['theme'].lower()}.",
            
            f"A {elements['genre']} story where a {elements['character_type'].lower()} in {elements['setting']} must overcome {elements['conflict'].lower()} to achieve {elements['plot_device'].lower()}, exploring the theme of {elements['theme'].lower()}.",
            
            f"What happens when a {elements['character_type'].lower()} confronts {elements['conflict'].lower()} in {elements['setting']}? This {elements['genre'].lower()} explores {elements['theme'].lower()} through the lens of {elements['plot_device'].lower()}.",
            
            f"The {elements['setting']} becomes the backdrop for a {elements['genre'].lower()} where {elements['theme'].lower()} is tested when a {elements['character_type'].lower()} experiences {elements['plot_device'].lower()} amid {elements['conflict'].lower()}.",
            
            f"A tale of {elements['theme'].lower()} unfolds in this {elements['genre'].lower()} set in {elements['setting']}, following a {elements['character_type'].lower()} who encounters {elements['conflict'].lower()} during {elements['plot_device'].lower()}."
        ]
        
        return random.choice(prompts)
    
    def generate_variations(self, base_idea: Dict[str, str], count: int = 3) -> List[str]:
        """Generate variations of a story idea"""
        variations = []
        original_elements = base_idea.copy()
        
        for _ in range(count):
            # Modify 2-3 elements to create a variation
            elements = original_elements.copy()
            num_changes = random.randint(2, 3)
            keys_to_change = random.sample(list(elements.keys()), num_changes)
            
            for key in keys_to_change:
                if key == "genre":
                    elements[key] = random.choice([g for g in self.genres if g != elements[key]])
                elif key == "character_type":
                    elements[key] = random.choice([c for c in self.character_types if c != elements[key]])
                elif key == "plot_device":
                    elements[key] = random.choice([p for p in self.plot_devices if p != elements[key]])
                elif key == "setting":
                    elements[key] = random.choice([s for s in self.settings if s != elements[key]])
                elif key == "theme":
                    elements[key] = random.choice([t for t in self.themes if t != elements[key]])
                elif key == "conflict":
                    elements[key] = random.choice([c for c in self.conflicts if c != elements[key]])
            
            variations.append(self.create_prompt(elements))
        
        return variations
    
    def generate_sequel_idea(self, original_story: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a sequel based on an original story"""
        # Extract elements from the original story
        elements = original_story["elements"].copy()
        
        # Keep some elements consistent for continuity
        keep_consistent = random.sample(["genre", "setting", "character_type"], 2)
        
        # Change other elements to create a new but related story
        for key in elements:
            if key not in keep_consistent:
                if key == "genre":
                    elements[key] = random.choice([g for g in self.genres if g != elements[key]])
                elif key == "character_type":
                    elements[key] = random.choice([c for c in self.character_types if c != elements[key]])
                elif key == "plot_device":
                    elements[key] = random.choice([p for p in self.plot_devices if p != elements[key]])
                elif key == "setting":
                    elements[key] = random.choice([s for s in self.settings if s != elements[key]])
                elif key == "theme":
                    elements[key] = random.choice([t for t in self.themes if t != elements[key]])
                elif key == "conflict":
                    elements[key] = random.choice([c for c in self.conflicts if c != elements[key]])
        
        # Create sequel-specific prompts
        sequel_templates = [
            f"Continuing from where we left off in {original_story['title']}, our {elements['character_type'].lower()} now faces {elements['conflict'].lower()} while dealing with the consequences of {original_story['elements']['plot_device'].lower()}.",
            
            f"Years after the events of {original_story['title']}, {elements['setting']} has changed. A new {elements['plot_device'].lower()} emerges, forcing our protagonist to confront {elements['conflict'].lower()} once again.",
            
            f"The saga continues as {elements['theme'].lower()} takes center stage in this sequel to {original_story['title']}. Our {elements['character_type'].lower()} must navigate {elements['conflict'].lower()} in an evolving {elements['setting']}."
        ]
        
        return {
            "title": f"{original_story['title']}: The Sequel",
            "prompt": random.choice(sequel_templates),
            "elements": elements,
            "original_story": original_story['title']
        }
    
    def evolve_narrative(self, story_id: int, direction: str) -> Dict[str, Any]:
        """Evolve a narrative in a specific direction based on user input"""
        if story_id >= len(self.story_history):
            raise ValueError(f"Story ID {story_id} not found in history")
        
        original_story = self.story_history[story_id]
        elements = original_story["elements"].copy()
        
        # Modify the story based on the direction
        if direction.lower() == "darker":
            # Make the story darker
            elements["genre"] = random.choice(["Horror", "Thriller", "Mystery", "Drama"])
            elements["theme"] = random.choice(["Betrayal", "Survival", "Power", "Justice"])
            elements["conflict"] = random.choice(["Person vs. Person", "Person vs. Self", "Person vs. Society"])
            
            evolution_templates = [
                f"As shadows lengthen in {elements['setting']}, our {elements['character_type'].lower()} discovers a sinister truth behind {original_story['elements']['plot_device'].lower()}, leading to a confrontation with {elements['conflict'].lower()}.",
                
                f"The once hopeful tale takes a grim turn as {elements['theme'].lower()} reveals its darker side. In {elements['setting']}, the {elements['character_type'].lower()} must face {elements['conflict'].lower()} with diminishing options.",
                
                f"What began as {original_story['title']} now descends into darkness. The {elements['character_type'].lower()} finds that {elements['plot_device'].lower()} comes with a terrible price in this exploration of {elements['theme'].lower()}."
            ]
            
        elif direction.lower() == "hopeful":
            # Make the story more hopeful
            elements["genre"] = random.choice(["Fantasy", "Adventure", "Romance", "Comedy"])
            elements["theme"] = random.choice(["Love", "Redemption", "Freedom", "Family"])
            elements["conflict"] = random.choice(["Person vs. Nature", "Person vs. Technology", "Person vs. Fate"])
            
            evolution_templates = [
                f"Light breaks through the challenges of {original_story['title']} as our {elements['character_type'].lower()} discovers new allies in {elements['setting']}. Together they transform {elements['conflict'].lower()} into an opportunity for {elements['theme'].lower()}.",
                
                f"The journey continues with renewed purpose as the {elements['character_type'].lower()} embraces {elements['plot_device'].lower()} with fresh perspective. In {elements['setting']}, {elements['theme'].lower()} blossoms despite {elements['conflict'].lower()}.",
                
                f"Rising from the trials of {original_story['title']}, our protagonist finds that {elements['setting']} holds unexpected wonders. This tale of {elements['theme'].lower()} shows how {elements['conflict'].lower()} can lead to growth and connection."
            ]
            
        elif direction.lower() == "complex":
            # Make the story more complex
            elements["genre"] = random.choice(["Science Fiction", "Historical Fiction", "Mystery", "Drama"])
            elements["theme"] = random.choice(["Identity", "Power", "Justice", "Reality"])
            elements["conflict"] = random.choice(["Person vs. Society", "Person vs. Reality", "Person vs. Self"])
            
            evolution_templates = [
                f"The seemingly straightforward tale of {original_story['title']} unravels to reveal intricate layers. In {elements['setting']}, our {elements['character_type'].lower()} discovers that {elements['plot_device'].lower()} connects to a web of {elements['theme'].lower()} and {elements['conflict'].lower()}.",
                
                f"As perspectives shift in {elements['setting']}, the line between right and wrong blurs. The {elements['character_type'].lower()} must navigate moral ambiguities of {elements['theme'].lower()} while confronting {elements['conflict'].lower()} from multiple angles.",
                
                f"What seemed like a single thread of {elements['plot_device'].lower()} now reveals itself as a tapestry. Our protagonist's journey through {elements['setting']} becomes an exploration of {elements['theme'].lower()} with no easy answers to {elements['conflict'].lower()}."
            ]
            
        else:  # "action"
            # Make the story more action-oriented
            elements["genre"] = random.choice(["Adventure", "Thriller", "Science Fiction", "Fantasy"])
            elements["theme"] = random.choice(["Survival", "Justice", "Power", "Freedom"])
            elements["conflict"] = random.choice(["Person vs. Person", "Person vs. Nature", "Person vs. Supernatural"])
            
            evolution_templates = [
                f"The stakes escalate rapidly in {elements['setting']} as our {elements['character_type'].lower()} is thrust into a high-octane confrontation. {elements['plot_device'].lower()} becomes a race against time amid intense {elements['conflict'].lower()}.",
                
                f"Danger erupts in {elements['setting']} when {elements['plot_device'].lower()} attracts powerful enemies. The {elements['character_type'].lower()} must master new skills to survive {elements['conflict'].lower()} in this adrenaline-fueled chapter of {elements['theme'].lower()}.",
                
                f"From the foundations of {original_story['title']} emerges a battle for survival. In {elements['setting']}, our protagonist faces relentless {elements['conflict'].lower()} that transforms {elements['theme'].lower()} into a trial by fire."
            ]
        
        return {
            "title": f"{original_story['title']}: Evolved",
            "prompt": random.choice(evolution_templates),
            "elements": elements,
            "original_story": original_story['title'],
            "evolution_direction": direction
        }
    
    def generate_story_ideas(self, count: int = 5) -> List[Dict[str, Any]]:
        """Generate multiple story ideas with variations"""
        story_ideas = []
        
        for i in range(count):
            # Generate base idea
            base_elements = self.generate_basic_idea()
            base_prompt = self.create_prompt(base_elements)
            
            # Generate variations
            variations = self.generate_variations(base_elements)
            
            # Create a title
            words = base_prompt.split()
            title_words = random.sample([w for w in words if len(w) > 3], min(3, len([w for w in words if len(w) > 3])))
            title = "The " + " ".join(title_words).replace(".", "").replace(",", "")
            
            story_idea = {
                "id": len(self.story_history),
                "title": title,
                "prompt": base_prompt,
                "elements": base_elements,
                "variations": variations
            }
            
            story_ideas.append(story_idea)
            self.story_history.append(story_idea)
        
        return story_ideas

    def save_to_file(self, filename: str = "story_ideas.json"):
        """Save generated story ideas to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.story_history, f, indent=4)

    def load_from_file(self, filename: str = "story_ideas.json") -> bool:
        """Load story ideas from a JSON file"""
        try:
            with open(filename, 'r') as f:
                self.story_history = json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False


def display_story_idea(idea: Dict[str, Any]):
    """Display a story idea in a formatted way"""
    print(f"\n{'='*80}")
    print(f"STORY IDEA #{idea['id']}: {idea['title']}")
    print(f"{'='*80}")
    print(f"\nPROMPT:\n{idea['prompt']}\n")
    
    print("ELEMENTS:")
    for key, value in idea['elements'].items():
        print(f"  {key.capitalize()}: {value}")
    
    print("\nVARIATIONS:")
    for i, variation in enumerate(idea['variations'], 1):
        print(f"  {i}. {variation}")
    
    if "original_story" in idea:
        print(f"\nBased on: {idea['original_story']}")
    
    if "evolution_direction" in idea:
        print(f"Evolution Direction: {idea['evolution_direction']}")


def main():
    generator = StoryIdeaGenerator()
    
    while True:
        print("\n" + "*"*80)
        print("STORY IDEA GENERATOR")
        print("*"*80)
        print("\nOptions:")
        print("1. Generate new story ideas")
        print("2. Create a sequel to an existing story")
        print("3. Evolve a narrative in a specific direction")
        print("4. Save ideas to file")
        print("5. Load ideas from file")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            count = int(input("How many story ideas would you like to generate? "))
            ideas = generator.generate_story_ideas(count)
            
            for idea in ideas:
                display_story_idea(idea)
                input("\nPress Enter to continue...")
        
        elif choice == "2":
            if not generator.story_history:
                print("\nNo existing stories to create a sequel from. Generate some stories first.")
                continue
            
            print("\nExisting stories:")
            for i, story in enumerate(generator.story_history):
                print(f"{i}. {story['title']}")
            
            story_id = int(input("\nEnter the ID of the story to create a sequel for: "))
            
            if 0 <= story_id < len(generator.story_history):
                sequel = generator.generate_sequel_idea(generator.story_history[story_id])
                generator.story_history.append(sequel)
                sequel["id"] = len(generator.story_history) - 1
                display_story_idea(sequel)
            else:
                print("Invalid story ID.")
        
        elif choice == "3":
            if not generator.story_history:
                print("\nNo existing stories to evolve. Generate some stories first.")
                continue
            
            print("\nExisting stories:")
            for i, story in enumerate(generator.story_history):
                print(f"{i}. {story['title']}")
            
            story_id = int(input("\nEnter the ID of the story to evolve: "))
            
            if 0 <= story_id < len(generator.story_history):
                print("\nEvolution directions:")
                print("1. Darker - Make the story more grim or serious")
                print("2. Hopeful - Make the story more optimistic or uplifting")
                print("3. Complex - Add moral ambiguity or philosophical depth")
                print("4. Action - Increase the pace and add more conflict")
                
                direction_choice = input("\nChoose a direction (1-4): ")
                direction_map = {"1": "darker", "2": "hopeful", "3": "complex", "4": "action"}
                
                if direction_choice in direction_map:
                    evolved = generator.evolve_narrative(story_id, direction_map[direction_choice])
                    generator.story_history.append(evolved)
                    evolved["id"] = len(generator.story_history) - 1
                    display_story_idea(evolved)
                else:
                    print("Invalid direction choice.")
            else:
                print("Invalid story ID.")
        
        elif choice == "4":
            filename = input("Enter filename to save (default: story_ideas.json): ") or "story_ideas.json"
            generator.save_to_file(filename)
            print(f"\nSaved {len(generator.story_history)} story ideas to {filename}")
        
        elif choice == "5":
            filename = input("Enter filename to load (default: story_ideas.json): ") or "story_ideas.json"
            if generator.load_from_file(filename):
                print(f"\nLoaded {len(generator.story_history)} story ideas from {filename}")
            else:
                print(f"\nFailed to load from {filename}")
        
        elif choice == "6":
            print("\nThank you for using the Story Idea Generator!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
