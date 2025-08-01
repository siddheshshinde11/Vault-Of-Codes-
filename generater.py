import random
import json
from datetime import datetime

class BusinessIdeaGenerator:
    def __init__(self):
        # Industries with specific niches
        self.industries = {
            "Technology": ["AI", "Blockchain", "IoT", "AR/VR", "Cybersecurity", "Edge Computing", "Quantum Computing"],
            "Health": ["Telemedicine", "Mental Health", "Preventive Care", "Elder Care", "Fitness Tech", "Nutrition", "Medical Devices"],
            "Education": ["E-learning", "Skill Development", "Early Childhood", "Professional Training", "Language Learning", "Educational Games"],
            "Food": ["Plant-based", "Meal Kits", "Ghost Kitchens", "Specialty Diets", "Artisanal Products", "Food Waste Reduction"],
            "Retail": ["D2C Brands", "Sustainable Fashion", "Personalized Shopping", "Rental Services", "Resale Markets", "Pop-up Stores"],
            "Finance": ["Microfinance", "Personal Finance", "Crypto", "Insurtech", "Wealth Management", "Financial Literacy"],
            "Entertainment": ["Streaming Content", "Podcasts", "Interactive Media", "Gaming", "Virtual Events", "Creator Economy"],
            "Sustainability": ["Renewable Energy", "Circular Economy", "Carbon Capture", "Sustainable Packaging", "Water Conservation"]
        }
        
        # Audience demographics and psychographics
        self.audiences = {
            "Demographics": {
                "Age": ["Gen Z (18-24)", "Millennials (25-40)", "Gen X (41-56)", "Baby Boomers (57-75)", "Seniors (76+)"],
                "Income": ["Budget-conscious", "Middle income", "Affluent", "High net worth"],
                "Location": ["Urban", "Suburban", "Rural", "Remote", "International"],
                "Occupation": ["Students", "Professionals", "Entrepreneurs", "Freelancers", "Retirees", "Homemakers"]
            },
            "Psychographics": {
                "Values": ["Sustainability", "Convenience", "Luxury", "Innovation", "Community", "Health-conscious", "Privacy-focused"],
                "Interests": ["Tech enthusiasts", "Health & wellness", "Outdoor activities", "Arts & culture", "DIY & crafts", "Travel", "Food & cooking"],
                "Pain Points": ["Time scarcity", "Budget constraints", "Information overload", "Social isolation", "Health concerns", "Environmental anxiety"]
            }
        }
        
        # Current and emerging trends
        self.trends = {
            "Technology Trends": ["AI automation", "Voice interfaces", "No-code tools", "Digital privacy", "Metaverse", "Web3", "Sustainable tech"],
            "Consumer Trends": ["Subscription economy", "Personalization", "Ethical consumption", "Remote work", "Digital wellness", "Contactless services"],
            "Economic Trends": ["Gig economy", "Circular economy", "Local sourcing", "Micro-entrepreneurship", "Collaborative consumption"],
            "Social Trends": ["Community building", "Social impact", "Diversity & inclusion", "Digital communities", "Creator economy"]
        }
        
        # Business models
        self.business_models = [
            "Subscription", "Marketplace", "Freemium", "On-demand service", "Direct-to-consumer", 
            "Sharing economy", "Membership", "Pay-per-use", "White-label", "Franchise", 
            "Advertising-based", "Affiliate marketing", "SaaS", "PaaS", "Data monetization"
        ]
        
        # Revenue streams
        self.revenue_streams = [
            "Monthly subscriptions", "One-time purchases", "Transaction fees", "Premium features", 
            "Advertising", "Sponsorships", "Licensing", "Consulting services", "Data insights", 
            "Affiliate commissions", "Crowdfunding", "Grants", "Enterprise contracts"
        ]
        
        # Real-world constraints
        self.constraints = {
            "Market": ["High competition", "Regulatory hurdles", "High customer acquisition costs", "Market saturation", "Changing consumer preferences"],
            "Operational": ["Supply chain complexity", "Talent shortage", "High operational costs", "Scalability challenges", "Quality control"],
            "Financial": ["High startup costs", "Long path to profitability", "Funding challenges", "Seasonal cash flow", "Currency fluctuations"],
            "Technological": ["Technical complexity", "Integration challenges", "Rapid obsolescence", "Cybersecurity risks", "Data privacy concerns"]
        }

    def get_random_item(self, dictionary, key=None):
        """Get a random item from a dictionary, optionally from a specific key"""
        if key:
            if isinstance(dictionary[key], list):
                return random.choice(dictionary[key])
            else:
                sub_key = random.choice(list(dictionary[key].keys()))
                return random.choice(dictionary[key][sub_key])
        else:
            main_key = random.choice(list(dictionary.keys()))
            if isinstance(dictionary[main_key], list):
                return main_key, random.choice(dictionary[main_key])
            else:
                sub_key = random.choice(list(dictionary[main_key].keys()))
                return main_key, sub_key, random.choice(dictionary[main_key][sub_key])

    def generate_idea_from_industry(self, industry=None, niche=None):
        """Generate a business idea based on a specific industry"""
        if not industry:
            industry, niche = self.get_random_item(self.industries)
        elif not niche and industry in self.industries:
            niche = random.choice(self.industries[industry])
        
        # Get random audience
        demo_category = random.choice(list(self.audiences["Demographics"].keys()))
        demographic = random.choice(self.audiences["Demographics"][demo_category])
        psycho_category = random.choice(list(self.audiences["Psychographics"].keys()))
        psychographic = random.choice(self.audiences["Psychographics"][psycho_category])
        
        # Get random trend
        trend_category = random.choice(list(self.trends.keys()))
        trend = random.choice(self.trends[trend_category])
        
        # Get business model and revenue stream
        business_model = random.choice(self.business_models)
        revenue_stream = random.choice(self.revenue_streams)
        
        # Get constraints
        constraint_category = random.choice(list(self.constraints.keys()))
        constraint = random.choice(self.constraints[constraint_category])
        
        # Generate the idea
        idea = self._format_idea(industry, niche, demographic, psychographic, trend, business_model, revenue_stream, constraint)
        return idea

    def generate_idea_from_audience(self, demographic=None, psychographic=None):
        """Generate a business idea based on a specific audience"""
        if not demographic:
            demo_category = random.choice(list(self.audiences["Demographics"].keys()))
            demographic = random.choice(self.audiences["Demographics"][demo_category])
        
        if not psychographic:
            psycho_category = random.choice(list(self.audiences["Psychographics"].keys()))
            psychographic = random.choice(self.audiences["Psychographics"][psycho_category])
        
        # Get random industry
        industry, niche = self.get_random_item(self.industries)
        
        # Get random trend
        trend_category = random.choice(list(self.trends.keys()))
        trend = random.choice(self.trends[trend_category])
        
        # Get business model and revenue stream
        business_model = random.choice(self.business_models)
        revenue_stream = random.choice(self.revenue_streams)
        
        # Get constraints
        constraint_category = random.choice(list(self.constraints.keys()))
        constraint = random.choice(self.constraints[constraint_category])
        
        # Generate the idea
        idea = self._format_idea(industry, niche, demographic, psychographic, trend, business_model, revenue_stream, constraint)
        return idea

    def generate_idea_from_trend(self, trend=None):
        """Generate a business idea based on a specific trend"""
        if not trend:
            trend_category = random.choice(list(self.trends.keys()))
            trend = random.choice(self.trends[trend_category])
        
        # Get random industry
        industry, niche = self.get_random_item(self.industries)
        
        # Get random audience
        demo_category = random.choice(list(self.audiences["Demographics"].keys()))
        demographic = random.choice(self.audiences["Demographics"][demo_category])
        psycho_category = random.choice(list(self.audiences["Psychographics"].keys()))
        psychographic = random.choice(self.audiences["Psychographics"][psycho_category])
        
        # Get business model and revenue stream
        business_model = random.choice(self.business_models)
        revenue_stream = random.choice(self.revenue_streams)
        
        # Get constraints
        constraint_category = random.choice(list(self.constraints.keys()))
        constraint = random.choice(self.constraints[constraint_category])
        
        # Generate the idea
        idea = self._format_idea(industry, niche, demographic, psychographic, trend, business_model, revenue_stream, constraint)
        return idea

    def _format_idea(self, industry, niche, demographic, psychographic, trend, business_model, revenue_stream, constraint):
        """Format the business idea into a structured output"""
        # Generate a creative name
        name_elements = [niche, demographic, psychographic, trend]
        random.shuffle(name_elements)
        business_name = f"{random.choice(name_elements).split()[0]}{random.choice(['Hub', 'Go', 'Ly', 'ify', 'Wise', 'Now', 'Sync', 'Pulse'])}"
        
        # Generate a concise description
        description = f"A {business_model.lower()} business offering {niche.lower()} solutions for {demographic.lower()} who are {psychographic.lower()}, capitalizing on the {trend.lower()} trend."
        
        # Generate unique value proposition
        value_props = [
            f"Tailored specifically for {demographic}",
            f"Addresses the unique needs of {psychographic} individuals",
            f"Leverages cutting-edge {niche} technology",
            f"Rides the wave of {trend}",
            f"Disrupts traditional {industry.lower()} with innovative approach"
        ]
        random.shuffle(value_props)
        value_proposition = value_props[:3]
        
        # Generate potential challenges and solutions
        challenge = f"Challenge: {constraint}"
        solutions = [
            "Strategic partnerships to share resources and reduce costs",
            "Phased implementation approach to test market response",
            "Freemium model to build user base before monetization",
            "Community-building focus to reduce marketing costs",
            "Leveraging existing platforms instead of building from scratch",
            "Focusing on a highly specific niche to avoid direct competition"
        ]
        solution = f"Potential Solution: {random.choice(solutions)}"
        
        # Format the complete idea
        idea = {
            "business_name": business_name,
            "concept": {
                "industry": industry,
                "niche": niche,
                "target_audience": {
                    "demographic": demographic,
                    "psychographic": psychographic
                },
                "trend": trend,
                "business_model": business_model,
                "revenue_stream": revenue_stream
            },
            "description": description,
            "value_proposition": value_proposition,
            "real_world_constraints": {
                "challenge": constraint,
                "solution": solution
            },
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return idea

    def generate_collection(self, count=5, method="mixed"):
        """Generate a collection of business ideas"""
        collection = []
        
        for _ in range(count):
            if method == "industry":
                idea = self.generate_idea_from_industry()
            elif method == "audience":
                idea = self.generate_idea_from_audience()
            elif method == "trend":
                idea = self.generate_idea_from_trend()
            else:  # mixed
                choice = random.choice(["industry", "audience", "trend"])
                if choice == "industry":
                    idea = self.generate_idea_from_industry()
                elif choice == "audience":
                    idea = self.generate_idea_from_audience()
                else:
                    idea = self.generate_idea_from_trend()
            
            collection.append(idea)
        
        return collection

    def save_collection(self, collection, filename="business_ideas.json"):
        """Save the collection to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(collection, f, indent=4)
        print(f"Collection saved to {filename}")

    def print_idea(self, idea):
        """Print a formatted business idea"""
        print(f"\n{'='*50}")
        print(f"BUSINESS IDEA: {idea['business_name']}")
        print(f"{'='*50}")
        print(f"CONCEPT:")
        print(f"  Industry: {idea['concept']['industry']} (Niche: {idea['concept']['niche']})")
        print(f"  Target Audience: {idea['concept']['target_audience']['demographic']} who are {idea['concept']['target_audience']['psychographic']}")
        print(f"  Trend: {idea['concept']['trend']}")
        print(f"  Business Model: {idea['concept']['business_model']}")
        print(f"  Revenue Stream: {idea['concept']['revenue_stream']}")
        print(f"\nDESCRIPTION:\n  {idea['description']}")
        print(f"\nVALUE PROPOSITION:")
        for i, prop in enumerate(idea['value_proposition'], 1):
            print(f"  {i}. {prop}")
        print(f"\nREAL-WORLD CONSTRAINTS:")
        print(f"  {idea['real_world_constraints']['challenge']}")
        print(f"  {idea['real_world_constraints']['solution']}")
        print(f"\nGenerated at: {idea['generated_at']}")
        print(f"{'='*50}\n")

    def print_collection(self, collection):
        """Print a collection of business ideas"""
        for idea in collection:
            self.print_idea(idea)


def main():
    generator = BusinessIdeaGenerator()
    
    print("\nBUSINESS IDEA GENERATOR")
    print("=======================")
    print("This program generates innovative business ideas based on industry, audience, or trend.")
    
    while True:
        print("\nGENERATION OPTIONS:")
        print("1. Generate based on industry")
        print("2. Generate based on audience")
        print("3. Generate based on trend")
        print("4. Generate a mixed collection")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            # List available industries
            print("\nAvailable Industries:")
            for i, industry in enumerate(generator.industries.keys(), 1):
                print(f"{i}. {industry}")
            
            industry_choice = input("\nSelect an industry (enter number or leave blank for random): ")
            
            if industry_choice.strip() and industry_choice.isdigit() and 1 <= int(industry_choice) <= len(generator.industries):
                industry = list(generator.industries.keys())[int(industry_choice) - 1]
                
                # List niches for the selected industry
                print(f"\nNiches for {industry}:")
                for i, niche in enumerate(generator.industries[industry], 1):
                    print(f"{i}. {niche}")
                
                niche_choice = input("\nSelect a niche (enter number or leave blank for random): ")
                
                if niche_choice.strip() and niche_choice.isdigit() and 1 <= int(niche_choice) <= len(generator.industries[industry]):
                    niche = generator.industries[industry][int(niche_choice) - 1]
                    idea = generator.generate_idea_from_industry(industry, niche)
                else:
                    idea = generator.generate_idea_from_industry(industry)
            else:
                idea = generator.generate_idea_from_industry()
            
            generator.print_idea(idea)
            
        elif choice == "2":
            # List demographic categories
            print("\nDemographic Categories:")
            for i, category in enumerate(generator.audiences["Demographics"].keys(), 1):
                print(f"{i}. {category}")
            
            demo_cat_choice = input("\nSelect a demographic category (enter number or leave blank for random): ")
            
            demographic = None
            if demo_cat_choice.strip() and demo_cat_choice.isdigit() and 1 <= int(demo_cat_choice) <= len(generator.audiences["Demographics"]):
                demo_category = list(generator.audiences["Demographics"].keys())[int(demo_cat_choice) - 1]
                
                # List options for the selected demographic category
                print(f"\nOptions for {demo_category}:")
                for i, option in enumerate(generator.audiences["Demographics"][demo_category], 1):
                    print(f"{i}. {option}")
                
                demo_choice = input("\nSelect a demographic (enter number or leave blank for random): ")
                
                if demo_choice.strip() and demo_choice.isdigit() and 1 <= int(demo_choice) <= len(generator.audiences["Demographics"][demo_category]):
                    demographic = generator.audiences["Demographics"][demo_category][int(demo_choice) - 1]
            
            # List psychographic categories
            print("\nPsychographic Categories:")
            for i, category in enumerate(generator.audiences["Psychographics"].keys(), 1):
                print(f"{i}. {category}")
            
            psycho_cat_choice = input("\nSelect a psychographic category (enter number or leave blank for random): ")
            
            psychographic = None
            if psycho_cat_choice.strip() and psycho_cat_choice.isdigit() and 1 <= int(psycho_cat_choice) <= len(generator.audiences["Psychographics"]):
                psycho_category = list(generator.audiences["Psychographics"].keys())[int(psycho_cat_choice) - 1]
                
                # List options for the selected psychographic category
                print(f"\nOptions for {psycho_category}:")
                for i, option in enumerate(generator.audiences["Psychographics"][psycho_category], 1):
                    print(f"{i}. {option}")
                
                psycho_choice = input("\nSelect a psychographic (enter number or leave blank for random): ")
                
                if psycho_choice.strip() and psycho_choice.isdigit() and 1 <= int(psycho_choice) <= len(generator.audiences["Psychographics"][psycho_category]):
                    psychographic = generator.audiences["Psychographics"][psycho_category][int(psycho_choice) - 1]
            
            idea = generator.generate_idea_from_audience(demographic, psychographic)
            generator.print_idea(idea)
            
        elif choice == "3":
            # List trend categories
            print("\nTrend Categories:")
            for i, category in enumerate(generator.trends.keys(), 1):
                print(f"{i}. {category}")
            
            trend_cat_choice = input("\nSelect a trend category (enter number or leave blank for random): ")
            
            trend = None
            if trend_cat_choice.strip() and trend_cat_choice.isdigit() and 1 <= int(trend_cat_choice) <= len(generator.trends):
                trend_category = list(generator.trends.keys())[int(trend_cat_choice) - 1]
                
                # List trends for the selected category
                print(f"\nTrends in {trend_category}:")
                for i, t in enumerate(generator.trends[trend_category], 1):
                    print(f"{i}. {t}")
                
                trend_choice = input("\nSelect a trend (enter number or leave blank for random): ")
                
                if trend_choice.strip() and trend_choice.isdigit() and 1 <= int(trend_choice) <= len(generator.trends[trend_category]):
                    trend = generator.trends[trend_category][int(trend_choice) - 1]
            
            idea = generator.generate_idea_from_trend(trend)
            generator.print_idea(idea)
            
        elif choice == "4":
            count = input("\nHow many ideas would you like to generate? (default: 5): ")
            count = int(count) if count.strip() and count.isdigit() and int(count) > 0 else 5
            
            method = input("\nGeneration method (industry, audience, trend, or mixed - default: mixed): ").lower()
            if method not in ["industry", "audience", "trend", "mixed"]:
                method = "mixed"
            
            collection = generator.generate_collection(count, method)
            generator.print_collection(collection)
            
            save = input("\nWould you like to save this collection? (y/n): ").lower()
            if save == "y":
                filename = input("Enter filename (default: business_ideas.json): ")
                filename = filename if filename.strip() else "business_ideas.json"
                generator.save_collection(collection, filename)
                
        elif choice == "5":
            print("\nThank you for using the Business Idea Generator!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
