import os
from typing import List, Dict, Optional
from semanticscholar import SemanticScholar

# Define a type alias for publication data
PublicationData = Dict[str, Optional[str]]

def fetch_publications(semantic_scholar_id: str) -> List[PublicationData]:
    """Fetch publications from Semantic Scholar API."""
    sch = SemanticScholar()

    try:
        # Fetch author information
        author = sch.get_author(semantic_scholar_id)
    except Exception as e:
        raise Exception(f"Failed to fetch author data: {e}")

    if not author:
        raise Exception(f"Author with Semantic Scholar ID {semantic_scholar_id} not found.")

    publications = []
    for paper in author['papers']:
        try:
            publication = {
                "title": paper.get('title', 'No Title'),
                "year": paper.get('year', 'Unknown'),
                "url": paper.get('url', ''),
                "authors": ', '.join([f"{a.get('name', '')}" for a in paper.get('authors', [])]),
                "journal": paper.get('journal', {}).get('name', 'Unknown'),
                "doi": paper.get('externalIds', {}).get('DOI', 'No DOI')
            }
            publications.append(publication)
        except AttributeError:
            continue

    return publications

def create_markdown(publications: List[PublicationData]) -> str:
    """Create a markdown file listing publications with detailed information."""
    markdown_content = "# Publications\n\n"

    # Organize publications by year
    publications_by_year: Dict[str, List[PublicationData]] = {}

    for paper in publications:
        # Extract year
        year = paper.get("year", "Unknown")

        # Extract title
        title = paper.get("title", "No Title")

        # Extract URL
        url = paper.get("url", "")

        # Extract authors
        authors = paper.get("authors", "Unknown")

        # Extract journal
        journal = paper.get("journal", "Unknown")

        # Extract DOI
        doi = paper.get("doi", "No DOI")

        if year not in publications_by_year:
            publications_by_year[year] = []
        publications_by_year[year].append({
            "title": title,
            "authors": authors,
            "journal": journal,
            "doi": doi,
            "link": url
        })

    # Generate Markdown content
    for year, works in sorted(publications_by_year.items(), reverse=True):
        markdown_content += f"## {year}\n\n"
        for work in works:
            markdown_content += f"### {work['title']}\n"
            markdown_content += f"- **Authors**: {work['authors']}\n"
            markdown_content += f"- **Journal**: {work['journal']}\n"
            markdown_content += f"- **DOI**: {work['doi']}\n"
            markdown_content += f"- **Link**: [View Publication]({work['link']})\n"
            markdown_content += "\n"

    return markdown_content

def save_markdown(content: str, filename: str) -> None:
    """Save markdown content to a file."""
    with open(filename, "w") as file:
        file.write(content)

def main(semantic_scholar_id: str, output_file: str) -> None:
    publications = fetch_publications(semantic_scholar_id)
    markdown_content = create_markdown(publications)
    save_markdown(markdown_content, output_file)
    print(f"Markdown file '{output_file}' created successfully.")

if __name__ == "__main__":
    semantic_scholar_id = "50614105"  # Replace with the Semantic Scholar ID of the author
    output_file = "../.markdown/publications.md"
    main(semantic_scholar_id, output_file)
