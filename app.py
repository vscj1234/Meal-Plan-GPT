from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Updated initialization
chat_model = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o-mini",
    max_tokens=1000
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user preferences
    data = request.json
    dietary_type = data.get('dietary_type')
    spice_level = data.get('spice_level')
    protein = data.get('protein')
    allergies = data.get('allergies')
    meal_type = data.get('meal_type')
    cuisine = data.get('cuisine')
    ingredients = data.get('ingredients')
    cooking_time = data.get('cooking_time')
    serving_size = data.get('serving_size')
    special_requests = data.get('special_requests')

    # Generate prompt for OpenAI with more specific instructions
    prompt = f"""You are an expert dietitian. Based on the following preferences, recommend tasty and health from the cuisine use selects dish:

User Preferences:
- Dietary Type: {dietary_type}
- Spice Level: {spice_level}
- Protein: {protein}
- Allergies/Restrictions: {allergies}
- Meal Type: {meal_type}
- Cuisine Origin: {cuisine}
- Ingredient Availability: {ingredients}
- Cooking Time: {cooking_time}
- Serving Size: {serving_size}
- Special Requests: {special_requests}

Please provide a detailed response in the following format:

1. Dish Name: [Name in English and Arabic/native language if applicable]
2. Cuisine Origin: [Specific country/region]
3. Ingredients List:
   - [List with quantities]
4. Step-by-step Recipe:
   - [Detailed steps]
5. Serving Suggestions:
   - [Presentation and accompaniments]
6. Nutritional Information:
   - Calories
   - Protein
   - Carbohydrates
   - Fat
   - Fiber
   - Vitamines and Minirals 

Ensure the recommendation respects all dietary restrictions and allergies mentioned."""

    try:
        # Get recommendation from OpenAI
        recommendation = chat_model.predict(prompt)
        return jsonify({'recommendation': recommendation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 