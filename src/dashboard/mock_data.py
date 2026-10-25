"""Fictional use-case records for the dashboard demo; not company research."""

from collections import Counter


FIRMS = (
    {"ticker": "JPM", "company": "JPMorgan Chase", "sector": "Banks"},
    {"ticker": "BAC", "company": "Bank of America", "sector": "Banks"},
    {"ticker": "COF", "company": "Capital One", "sector": "Banks"},
    {"ticker": "WFC", "company": "Wells Fargo", "sector": "Banks"},
    {"ticker": "C", "company": "Citigroup", "sector": "Banks", "cohort": "Benchmark"},
    {"ticker": "SCHW", "company": "Charles Schwab", "sector": "Broker-dealers & wealth"},
    {"ticker": "PFG", "company": "Principal Financial Group", "sector": "Retirement providers"},
)

DEMO_AREAS = (
    "Customer support",
    "Risk operations",
    "Employee productivity",
    "Client insights",
    "Document workflows",
)
DEMO_STAGES = ("Exploring", "Pilot", "In use")
ADDITIONAL_EXAMPLES = (
    ("JPM", "2024 Q1", "Sample form triage", "Document workflows", "Exploring"),
    ("JPM", "2024 Q3", "Fictional advisor briefing", "Client insights", "Pilot"),
    ("JPM", "2025 Q4", "Mock policy assistant", "Employee productivity", "Pilot"),
    ("JPM", "2026 Q2", "Simulated alert sorting", "Risk operations", "In use"),
    ("JPM", "2026 Q3", "Routine service response", "Customer support", "In use"),
    ("BAC", "2024 Q1", "Fictional help-center search", "Employee productivity", "Exploring"),
    ("BAC", "2024 Q2", "Sample account inquiry helper", "Customer support", "Pilot"),
    ("BAC", "2024 Q4", "Mock case prioritization", "Risk operations", "Pilot"),
    ("BAC", "2025 Q3", "Simulated policy document review", "Document workflows", "In use"),
    ("BAC", "2026 Q3", "Fictional client note summary", "Client insights", "In use"),
    ("COF", "2024 Q2", "Sample transaction review", "Risk operations", "Exploring"),
    ("COF", "2025 Q1", "Mock application document sort", "Document workflows", "Pilot"),
    ("COF", "2025 Q2", "Fictional service reply draft", "Customer support", "Pilot"),
    ("COF", "2025 Q4", "Sample staff knowledge search", "Employee productivity", "In use"),
    ("COF", "2026 Q2", "Mock advisor briefing", "Client insights", "In use"),
    ("WFC", "2024 Q1", "Fictional client note summary", "Client insights", "Exploring"),
    ("WFC", "2024 Q3", "Mock policy search", "Employee productivity", "Exploring"),
    ("WFC", "2025 Q1", "Sample form intake assistant", "Document workflows", "Pilot"),
    ("WFC", "2025 Q4", "Simulated service response", "Customer support", "Pilot"),
    ("WFC", "2026 Q3", "Mock investigation queue", "Risk operations", "In use"),
    ("C", "2024 Q1", "Sample service guide", "Customer support", "Exploring"),
    ("C", "2024 Q4", "Mock document routing", "Document workflows", "Pilot"),
    ("C", "2025 Q3", "Fictional policy search", "Employee productivity", "Pilot"),
    ("C", "2026 Q1", "Simulated portfolio note summary", "Client insights", "In use"),
    ("C", "2026 Q3", "Mock alert review queue", "Risk operations", "In use"),
    ("SCHW", "2024 Q1", "Sample participant service guide", "Customer support", "Exploring"),
    ("SCHW", "2024 Q2", "Mock document finder", "Document workflows", "Pilot"),
    ("SCHW", "2025 Q2", "Fictional alert triage", "Risk operations", "Pilot"),
    ("SCHW", "2025 Q4", "Sample client briefing", "Client insights", "In use"),
    ("SCHW", "2026 Q3", "Mock staff reference search", "Employee productivity", "In use"),
    ("PFG", "2024 Q2", "Fictional plan question guide", "Customer support", "Exploring"),
    ("PFG", "2024 Q4", "Mock plan document routing", "Document workflows", "Exploring"),
    ("PFG", "2025 Q2", "Sample advisor note summary", "Client insights", "Pilot"),
    ("PFG", "2025 Q3", "Simulated case review queue", "Risk operations", "Pilot"),
    ("PFG", "2026 Q3", "Fictional staff knowledge search", "Employee productivity", "In use"),
)

AREA_SUMMARIES = {
    "Customer support": "A fictional assistant drafts a response to a sample service question.",
    "Risk operations": "A mock workflow groups simulated alerts or cases for staff review.",
    "Employee productivity": "An invented internal assistant searches sample reference material.",
    "Client insights": "A mock assistant summarizes fictional advisor or client notes for review.",
    "Document workflows": "A prototype routes sample forms or documents to a staff queue.",
}

# These deliberately invented scenarios are UI examples attached to familiar firm names.
# They are not claims, evidence, labels, or research findings about those firms.
USE_CASES = (
    {
        "id": "JPM-01", "ticker": "JPM", "quarter": "2024 Q4",
        "title": "Service desk assistant", "area": "Customer support", "stage": "Exploring",
        "summary": "A virtual assistant suggests answers to routine account-service questions.",
        "detail": "A service representative reviews each suggested answer before it is sent.",
    },
    {
        "id": "JPM-02", "ticker": "JPM", "quarter": "2025 Q2",
        "title": "Transaction review queue", "area": "Risk operations", "stage": "Pilot",
        "summary": "A review tool sorts sample transactions into queues for staff attention.",
        "detail": "The mock workflow prioritizes review; a person makes every final decision.",
    },
    {
        "id": "JPM-03", "ticker": "JPM", "quarter": "2026 Q1",
        "title": "Internal knowledge search", "area": "Employee productivity", "stage": "In use",
        "summary": "An internal assistant helps staff find answers in a fictional policy library.",
        "detail": "This example demonstrates how a deployed-stage record might be explored.",
    },
    {
        "id": "BAC-01", "ticker": "BAC", "quarter": "2024 Q3",
        "title": "Contact-center reply helper", "area": "Customer support", "stage": "Exploring",
        "summary": "A draft assistant proposes responses for routine customer questions.",
        "detail": "A staff member edits or rejects every proposed response in this mock scenario.",
    },
    {
        "id": "BAC-02", "ticker": "BAC", "quarter": "2025 Q1",
        "title": "Document intake sorting", "area": "Document workflows", "stage": "Pilot",
        "summary": "A tool routes sample forms to the right processing team.",
        "detail": "The fictional pilot is meant to illustrate a record-level drill-down.",
    },
    {
        "id": "BAC-03", "ticker": "BAC", "quarter": "2026 Q2",
        "title": "Fraud alert review", "area": "Risk operations", "stage": "In use",
        "summary": "A review queue groups simulated alerts for investigators.",
        "detail": "The example is a user-interface scenario and does not describe Bank of America.",
    },
    {
        "id": "COF-01", "ticker": "COF", "quarter": "2024 Q4",
        "title": "Knowledge-base search", "area": "Employee productivity", "stage": "Exploring",
        "summary": "Staff test a search assistant over an invented internal help collection.",
        "detail": "This fictional early-stage record helps demonstrate the timeline.",
    },
    {
        "id": "COF-02", "ticker": "COF", "quarter": "2025 Q3",
        "title": "Customer conversation helper", "area": "Customer support", "stage": "Pilot",
        "summary": "A call assistant drafts a short recap for a service representative.",
        "detail": "A representative checks the recap before it is stored in the mock workflow.",
    },
    {
        "id": "COF-03", "ticker": "COF", "quarter": "2026 Q3",
        "title": "Case review prioritization", "area": "Risk operations", "stage": "In use",
        "summary": "A queue groups fictional cases to help staff plan their review workload.",
        "detail": "Priority in this made-up example is not a real risk score or company process.",
    },
    {
        "id": "WFC-01", "ticker": "WFC", "quarter": "2025 Q1",
        "title": "Form processing assistant", "area": "Document workflows", "stage": "Exploring",
        "summary": "A prototype extracts fields from sample documents for staff to check.",
        "detail": "The example shows how an exploratory record could be distinguished from a pilot.",
    },
    {
        "id": "WFC-02", "ticker": "WFC", "quarter": "2025 Q3",
        "title": "Routine inquiry assistant", "area": "Customer support", "stage": "Pilot",
        "summary": "A chat assistant guides users through a fictional set of routine questions.",
        "detail": "A person remains available to review or take over the mock interaction.",
    },
    {
        "id": "WFC-03", "ticker": "WFC", "quarter": "2026 Q1",
        "title": "Transaction review queue", "area": "Risk operations", "stage": "Exploring",
        "summary": "A sample queue groups simulated transactions for staff review.",
        "detail": "This is an invented example, not a description of Wells Fargo systems.",
    },
    {
        "id": "C-01", "ticker": "C", "quarter": "2024 Q2",
        "title": "Service conversation helper", "area": "Customer support", "stage": "Exploring",
        "summary": "A draft assistant suggests next steps in a fictional service conversation.",
        "detail": "This scenario is included to exercise comparisons, not to assert Citigroup use.",
    },
    {
        "id": "C-02", "ticker": "C", "quarter": "2025 Q2",
        "title": "Client portfolio briefing", "area": "Client insights", "stage": "Pilot",
        "summary": "A mock tool turns sample portfolio notes into a short client briefing.",
        "detail": "The hypothetical briefing is reviewed by an advisor before use.",
    },
    {
        "id": "C-03", "ticker": "C", "quarter": "2026 Q2",
        "title": "Alert investigation queue", "area": "Risk operations", "stage": "In use",
        "summary": "An example workflow groups sample alerts into an investigator queue.",
        "detail": "This record does not describe a real Citigroup tool, alert, or process.",
    },
    {
        "id": "SCHW-01", "ticker": "SCHW", "quarter": "2024 Q4",
        "title": "Advisor knowledge search", "area": "Employee productivity", "stage": "Exploring",
        "summary": "Advisors test search over a fictional set of reference materials.",
        "detail": "The mock search provides suggested links for an employee to review.",
    },
    {
        "id": "SCHW-02", "ticker": "SCHW", "quarter": "2025 Q3",
        "title": "Meeting recap assistant", "area": "Client insights", "stage": "Pilot",
        "summary": "A tool drafts a recap from a simulated client meeting.",
        "detail": "An advisor edits the fictional recap; no client data is used in this demo.",
    },
    {
        "id": "SCHW-03", "ticker": "SCHW", "quarter": "2026 Q1",
        "title": "Participant service guide", "area": "Customer support", "stage": "In use",
        "summary": "A guide suggests answers to a made-up set of plan-service questions.",
        "detail": "This example demonstrates detail navigation, not a claim about Schwab.",
    },
    {
        "id": "PFG-01", "ticker": "PFG", "quarter": "2025 Q1",
        "title": "Plan document helper", "area": "Document workflows", "stage": "Exploring",
        "summary": "A prototype helps staff locate sections in fictional plan documents.",
        "detail": "The hypothetical tool points to text for a staff member to verify.",
    },
    {
        "id": "PFG-02", "ticker": "PFG", "quarter": "2025 Q4",
        "title": "Participant question assistant", "area": "Customer support", "stage": "Pilot",
        "summary": "A mock assistant guides a participant through common plan questions.",
        "detail": "The example routes complex questions to a person for help.",
    },
    {
        "id": "PFG-03", "ticker": "PFG", "quarter": "2026 Q2",
        "title": "Plan-service knowledge search", "area": "Employee productivity", "stage": "Pilot",
        "summary": "A staff search assistant finds answers in an invented plan-service guide.",
        "detail": "This fictional pilot illustrates how multiple examples can share a stage.",
    },
)

USE_CASES += tuple(
    {
        "id": f"{ticker}-{index:02d}",
        "ticker": ticker,
        "quarter": quarter,
        "title": title,
        "area": area,
        "stage": stage,
        "summary": AREA_SUMMARIES[area],
        "detail": (
            f"This invented {stage.lower()} scenario exists only to demonstrate the dashboard; "
            "it does not describe the named firm."
        ),
    }
    for index, (ticker, quarter, title, area, stage) in enumerate(ADDITIONAL_EXAMPLES, start=4)
)


def get_firms(sector=None):
    """Return the selector firms, optionally filtered by sector."""
    return [firm.copy() for firm in FIRMS if sector is None or firm["sector"] == sector]


def get_use_cases(ticker=None):
    """Return fictional records, optionally for one selector firm."""
    return [
        record.copy()
        for record in USE_CASES
        if ticker is None or record["ticker"] == ticker
    ]


def summarize_use_cases(ticker):
    """Summarize only the fictional use-case records shown in the prototype."""
    records = get_use_cases(ticker)
    stage_counts = Counter(record["stage"] for record in records)
    latest = max(records, key=lambda record: record["quarter"]) if records else None
    areas = {record["area"] for record in records}
    return {
        "record_count": len(records),
        "area_count": len(areas),
        "stage_counts": dict(stage_counts),
        "latest_record": latest,
    }


def compare_use_cases(tickers):
    """Summarize mock records by firm, area, and stage for side-by-side comparison."""
    rows = []
    for firm in FIRMS:
        if firm["ticker"] not in tickers:
            continue
        records = get_use_cases(firm["ticker"])
        stages = Counter(record["stage"] for record in records)
        areas = Counter(record["area"] for record in records)
        rows.append({
            "company": firm["company"],
            "ticker": firm["ticker"],
            "sector": firm["sector"],
            "examples": len(records),
            "areas": ", ".join(sorted(areas)),
            "stage_counts": {stage: stages[stage] for stage in DEMO_STAGES},
            "area_counts": {area: areas[area] for area in DEMO_AREAS},
        })
    return rows


def compare_timeline(tickers):
    """Return cumulative fictional-record counts by quarter for selected firms."""
    quarter_key = lambda quarter: (
        int(quarter.split()[0]),
        int(quarter.split()[1][1:]),
    )
    quarters = sorted({record["quarter"] for record in USE_CASES}, key=quarter_key)
    rows = []
    for firm in FIRMS:
        ticker = firm["ticker"]
        if ticker not in tickers:
            continue
        records = get_use_cases(ticker)
        cumulative_count = 0
        for quarter in quarters:
            cumulative_count += sum(record["quarter"] == quarter for record in records)
            rows.append({
                "quarter": quarter,
                "ticker": ticker,
                "company": firm["company"],
                "cumulative_examples": cumulative_count,
            })
    return rows
