import argparse
from utils import extract_text, analyze_similarity

def main():
    parser = argparse.ArgumentParser(description="ATS Helper — Score CV vs JD")
    parser.add_argument('--cv', required=True, help='Path to the resume file')
    parser.add_argument('--job', required=True, help='Path to the job description')
    args = parser.parse_args()

    print("🔍 Analyzing...")
    cv_text = extract_text(args.cv)
    job_text = extract_text(args.job)

    results = analyze_similarity(cv_text, job_text)

    print("\n=== ATS RELEVANCE REPORT ===")
    print(f"✔️ Similarity Score: {results['score']:.2f}")
    print(f"🧠 Matching Keywords: {', '.join(results['matches'])}")
    print(f"🚩 Missing Keywords: {', '.join(results['missing'])}")
    print("============================")

if __name__ == "__main__":
    main()
