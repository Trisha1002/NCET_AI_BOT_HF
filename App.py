import streamlinen as st
from transformers import pipeline
@as.cache_resource
def load_summerizer();
  return pipeline("summarization", model="ssheifer/distilbart-cnn-12-6")

summerizer = load_summerize()
#Streamline UI
st.title(" AI Text Summerizer")
st.write("Enter a long text below, and get a concise summary!")
long_text = st.text_area("Enter text to summarizer:",height=200)

#Summary Parameters
max_length = st.slider("Max Summary Length", min_value=50,
                       max_value=300, value=130)
min_length = st.slider("Min Summary Length", min_value=20,
                       max_value=100, value=30)
if st.button("Summarize")
  if long_text.strip();
      with st.spinner("Generating summary... "):
        summary = summarizer(long_text, max_length,
                             min_length=min_length, do_sample=False)
        st.subheader(" Summary:")
        st.succes(summary[0] ['summary_text'])
else:
    st.warning(" Please enter some text to summarize.")
