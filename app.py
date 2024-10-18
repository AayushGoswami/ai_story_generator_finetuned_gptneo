import streamlit as st
from process import load_model, generate_story

# Set page config with custom theme
st.set_page_config(
    page_title="AI StoryWeaver",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "# AI StoryWeaver\n This is a story generation app."
    }
)


# Use st.cache_resource to ensure the model is loaded only once
@st.cache_resource
def get_model():
    model, device = load_model()
    return model, device

# Get the model and device
model, device = get_model()

# Streamlit UI
st.title("AI StoryWeaver - Interactive Story Generator 📖🔖")
st.write("Create your own stories with the help of an AI model fine-tuned for creative writing!")

# Expanded Genre and Tone selection
with st.sidebar:
    st.write(f"Using device: {device}")
    genre = st.selectbox("Select a genre for your story:", options=[
        "Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror",
        "Adventure", "Historical Fiction", "Thriller", "Comedy",
        "Drama", "Dystopian", "Fairy Tale", "Cyberpunk", "Western",
        "Superhero", "Paranormal", "Steampunk", "Urban Fantasy"
    ])
    tone = st.selectbox("Select the tone of your story:", options=[
        "Light-hearted", "Dark", "Mysterious", "Dramatic",
        "Humorous", "Whimsical", "Melancholic", "Suspenseful",
        "Inspirational", "Nostalgic", "Satirical", "Romantic",
        "Tragic", "Epic", "Philosophical", "Absurd", "Hopeful"
    ])

user_input = st.text_area("Write the beginning of your story, or simply give me an idea and I'll generate it!",
                          value=f"A {tone.lower()} {genre.lower()} story begins...")
max_length = st.slider("Select max story length:", min_value=50, max_value=500, value=100, step=10)
num_sequences = st.selectbox("Select number of stories to generate:", options=[1, 2, 3], index=0)

if st.button('Generate Story'):
    with st.spinner('Generating Story...'):
        response = generate_story(model, user_input, max_length, num_sequences)
        for i, summary in enumerate(response):
            st.write(f'**Story {i+1}:**')
            st.write(summary['generated_text'])
            st.markdown("---")

# Sidebar
st.sidebar.markdown("## Guide")
st.sidebar.info("This tool uses a fine-tuned GPT-Neo model to generate stories. Choose from a wide variety of genres and tones to inspire your story. Adjust the sliders to change the story length and number of stories generated.")
