from ticket_count import count_by_status


def test_counts_by_status(tmp_path):
    csv_file = tmp_path / "tickets.csv"
    csv_file.write_text(
        "ticket_id,customer_id,status,priority,created_at,subject\n"
        "T1,C1,open,high,2026-10-01,A\n"
        "T2,C2,open,low,2026-10-02,B\n"
        "T3,C1,closed,low,2026-10-03,C\n"
    )
    assert count_by_status(csv_file) == {"open": 2, "closed": 1}


def test_header_only_file(tmp_path):
    csv_file = tmp_path / "tickets.csv"
    csv_file.write_text("ticket_id,customer_id,status,priority,created_at,subject\n")
    assert count_by_status(csv_file) == {}