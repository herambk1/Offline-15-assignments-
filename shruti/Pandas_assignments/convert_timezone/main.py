import pandas as pd

data = {
    'emp_id': range(101, 131),
    'emp_name': [
        'Amit', 'Priya', 'Rahul', 'Sneha', 'Vijay',
        'Neha', 'Rohit', 'Pooja', 'Karan', 'Meera',
        'Arjun', 'Isha', 'Sahil', 'Kavya', 'Nikhil',
        'Ananya', 'Dev', 'Tanvi', 'Om', 'Riya',
        'Raj', 'Simran', 'Varun', 'Asha', 'Manish',
        'Payal', 'Akash', 'Swati', 'Nitin', 'Pallavi'
    ],
    'dept': [
        'IT', 'HR', 'Finance', 'IT', 'Sales',
        'HR', 'IT', 'Finance', 'Sales', 'IT',
        'HR', 'Finance', 'IT', 'Sales', 'HR',
        'IT', 'Finance', 'Sales', 'IT', 'HR',
        'Finance', 'IT', 'Sales', 'HR', 'IT',
        'Finance', 'Sales', 'IT', 'HR', 'Finance'
    ],
    'salary': [
        60000, 40000, 55000, 75000, 45000,
        42000, 80000, 65000, 48000, 90000,
        43000, 58000, 85000, 50000, 46000,
        95000, 62000, 52000, 78000, 44000,
        60000, 88000, 49000, 41000, 92000,
        57000, 53000, 82000, 47000, 64000
    ],
    'event_datetime': [
        '2026-10-01 01:00:00',
        '2026-10-01 03:30:00',
        '2026-10-01 06:00:00',
        '2026-10-01 08:15:00',
        '2026-10-01 10:45:00',
        '2026-10-02 00:30:00',
        '2026-10-02 02:00:00',
        '2026-10-02 04:30:00',
        '2026-10-02 07:00:00',
        '2026-10-02 09:30:00',
        '2026-10-03 01:15:00',
        '2026-10-03 03:45:00',
        '2026-10-03 06:30:00',
        '2026-10-03 08:00:00',
        '2026-10-03 11:30:00',
        '2026-10-04 00:00:00',
        '2026-10-04 02:45:00',
        '2026-10-04 05:15:00',
        '2026-10-04 07:45:00',
        '2026-10-04 10:00:00',
        '2026-10-05 01:30:00',
        '2026-10-05 04:00:00',
        '2026-10-05 06:45:00',
        '2026-10-05 09:15:00',
        '2026-10-05 12:00:00',
        '2026-10-06 00:45:00',
        '2026-10-06 03:15:00',
        '2026-10-06 05:45:00',
        '2026-10-06 08:30:00',
        '2026-10-06 11:00:00'
    ],
    'status': [
        'Active', 'Active', 'On Leave', 'Active', 'Active',
        'Active', 'Active', 'Resigned', 'Active', 'Active',
        'Active', 'Active', 'On Leave', 'Active', 'Active',
        'Active', 'Active', 'Resigned', 'Active', 'Active',
        'Active', 'Active', 'On Leave', 'Active', 'Active',
        'Active', 'Resigned', 'Active', 'Active', 'Active'
    ]
}
df = pd.DataFrame(data)

# str to utc
df['utc_datetime'] = pd.to_datetime(df['event_datetime'], utc=True)

# utc to ist
df['ist_datetime'] = df['utc_datetime'].dt.tz_convert('Asia/Kolkata')

# utc to sgt
df['sgt_datetime'] = df['utc_datetime'].dt.tz_convert('Asia/Singapore')

# utc to ust
df['ust_datetime'] = df['utc_datetime'].dt.tz_convert('America/Los_Angeles')

print(df[['ust_datetime', 'sgt_datetime', 'ist_datetime', 'utc_datetime']])

df.to_csv("timezone.csv", index=False)
