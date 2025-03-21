import streamlit as st
from pdf_processing import extract_text_from_pdf
from groq_api import groq_extract_info
from utils import save_results_to_json
from groq_api import MODEL_NAME

def main():
    """Application Streamlit pour l'extraction OCR avancée avec Groq Cloud."""
    st.title("📄 Extraction et Structuration Automatique d'Informations")
    
    with st.sidebar:
        st.header("Paramètres")
        st.sidebar.text(f"Modèle utilisé : {MODEL_NAME}")
    
    pdfs = st.file_uploader("📂 Upload de fichiers PDF", type='pdf', accept_multiple_files=True)
    
    if pdfs:
        with st.spinner("🔍 Extraction du texte..."):
            docs = extract_text_from_pdf(pdfs)
        
        if docs:
            st.success("✅ Extraction terminée !")
            
            if st.button("🚀 Analyser"):
                with st.spinner("🤖 Analyse en cours..."):
                    results = [groq_extract_info(doc) for doc in docs]
                
                # Afficher les résultats dans Streamlit
                st.header("📜 Résultats de l'analyse")
                for i, result in enumerate(results):
                    st.subheader(f"📄 Fichier {i+1}")
                    st.markdown(result)
                
                # Sauvegarde des résultats dans un fichier JSON
                save_results_to_json(docs, results)

                # Ajout du bouton pour télécharger le fichier JSON
                with open("extraction_results.json", "r") as f:
                    json_file = f.read()
                
                st.download_button(
                    label="Télécharger les résultats en JSON",
                    data=json_file,
                    file_name="extraction_results.json",
                    mime="application/json"
                )

if __name__ == "__main__":
    main()
