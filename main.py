import streamlit as st

# Brief description of the AHRQ Exercise Guidance for Primary Care Fall Prevention
st.title("AHRQ Exercise Guidance for Primary Care Fall Prevention")
st.markdown("""
## Introduction
Falls are a significant concern for older adults, often leading to severe injuries and reduced quality of life. To address this, the Agency for Healthcare Research and Quality (AHRQ) has developed comprehensive exercise guidance aimed at preventing falls in primary care settings. This guidance, created by Patty Dykes from Harvard University, emphasizes the importance of exercise in maintaining balance, strength, and overall physical health to reduce the risk of falls among older adults.

## Objectives
The primary objectives of this exercise guidance are:
- **Improve balance and coordination:** Regular exercise can help maintain and improve balance, reducing the likelihood of falls.
- **Increase strength:** Strength training exercises are crucial for enhancing muscle power, which supports better control and stability.
- **Enhance flexibility:** Flexibility exercises can help maintain a range of motion in the joints, making daily activities easier and safer.
- **Promote overall health:** Regular physical activity contributes to overall well-being, helping older adults stay active and independent.

## Key Exercises
The AHRQ exercise guidance includes a variety of exercises that can be easily incorporated into daily routines. Some of these exercises are:
- **Balance exercises:** Such as standing on one leg, heel-to-toe walking, and balance training with support.
- **Strength exercises:** Including chair rises, wall push-ups, and resistance band workouts.
- **Flexibility exercises:** Such as seated or standing stretches, focusing on the lower body, shoulders, and back.
- **Endurance exercises:** Including walking, cycling, and other aerobic activities that promote cardiovascular health.

## Recommendations
Primary care providers are encouraged to:
1. **Assess fall risk:** Regularly evaluate patients for their risk of falling using standardized tools and assessments.
2. **Promote exercise:** Recommend and guide patients to engage in the exercises outlined in the AHRQ guidance.
3. **Provide resources:** Offer educational materials and resources to help patients understand and implement these exercises effectively.
4. **Monitor progress:** Continuously monitor patients' progress and adjust exercise plans as needed to ensure effectiveness and safety.

## Conclusion
Implementing the AHRQ Exercise Guidance for Primary Care Fall Prevention can significantly reduce the risk of falls among older adults. By incorporating these exercises into regular care routines, primary care providers can help their patients maintain independence, improve quality of life, and prevent fall-related injuries.

For detailed exercise instructions and resources, visit the [AHRQ Fall Prevention Guide](https://www.ahrq.gov).
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Introduction", "Objectives", "Key Exercises", "Recommendations", "Conclusion"])

if options == "Introduction":
    st.subheader("Introduction")
    st.write("""
    Falls are a significant concern for older adults, often leading to severe injuries and reduced quality of life. To address this, the Agency for Healthcare Research and Quality (AHRQ) has developed comprehensive exercise guidance aimed at preventing falls in primary care settings. This guidance, created by Patty Dykes from Harvard University, emphasizes the importance of exercise in maintaining balance, strength, and overall physical health to reduce the risk of falls among older adults.
    """)
elif options == "Objectives":
    st.subheader("Objectives")
    st.write("""
    The primary objectives of this exercise guidance are:
    - Improve balance and coordination: Regular exercise can help maintain and improve balance, reducing the likelihood of falls.
    - Increase strength: Strength training exercises are crucial for enhancing muscle power, which supports better control and stability.
    - Enhance flexibility: Flexibility exercises can help maintain a range of motion in the joints, making daily activities easier and safer.
    - Promote overall health: Regular physical activity contributes to overall well-being, helping older adults stay active and independent.
    """)
elif options == "Key Exercises":
    st.subheader("Key Exercises")
    st.write("""
    The AHRQ exercise guidance includes a variety of exercises that can be easily incorporated into daily routines. Some of these exercises are:
    - Balance exercises: Such as standing on one leg, heel-to-toe walking, and balance training with support.
    - Strength exercises: Including chair rises, wall push-ups, and resistance band workouts.
    - Flexibility exercises: Such as seated or standing stretches, focusing on the lower body, shoulders, and back.
    - Endurance exercises: Including walking, cycling, and other aerobic activities that promote cardiovascular health.
    """)
elif options == "Recommendations":
    st.subheader("Recommendations")
    st.write("""
    Primary care providers are encouraged to:
    1. Assess fall risk: Regularly evaluate patients for their risk of falling using standardized tools and assessments.
    2. Promote exercise: Recommend and guide patients to engage in the exercises outlined in the AHRQ guidance.
    3. Provide resources: Offer educational materials and resources to help patients understand and implement these exercises effectively.
    4. Monitor progress: Continuously monitor patients' progress and adjust exercise plans as needed to ensure effectiveness and safety.
    """)
elif options == "Conclusion":
    st.subheader("Conclusion")
    st.write("""
    Implementing the AHRQ Exercise Guidance for Primary Care Fall Prevention can significantly reduce the risk of falls among older adults. By incorporating these exercises into regular care routines, primary care providers can help their patients maintain independence, improve quality of life, and prevent fall-related injuries.
    """)

# Footer
st.markdown("""
---
For detailed exercise instructions and resources, visit the [AHRQ Fall Prevention Guide](https://www.ahrq.gov).
""")
