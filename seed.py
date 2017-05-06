from model import Representative

from model import connect_to_db, db
from server import app


def load_rep():
    """Load representative information."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate data
    count = 0

    # Read file that contains 5 years of data and get all species.
    for row in open("legislators-current.csv"):
        if count != 0:
            row = row.rstrip()
            row = row.split(",")

            # Get the values from the row
            type_rep = row[4]

            # Check if legislator is senator or house rep

            last_name = row[0]
            first_name = row[1]
            state = row[5]
            district = row[6]
            party = row[7]

            representative = Representative(first_name=first_name,
                                            last_name=last_name,
                                            party=party,
                                            state=state,
                                            type_rep=type_rep,
                                            district=district)

            # Add to the session or it won't ever be stored
            db.session.add(representative)
        count += 1
    # Commit work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data. UNCOMMENT WHEN READY TO SEED FILE!!!!!!
    load_rep()
