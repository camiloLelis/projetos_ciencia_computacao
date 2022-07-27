from src import jobs


def get_unique_job_types(path):
    jobs_name = set()
    file_csv = jobs.read(path)
    for job in file_csv:
        jobs_name.add(job["job_type"])
    return jobs_name


def filter_by_job_type(jobs, job_type):
    array_filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            array_filter_job_type.append(job)
    return array_filter_job_type


def get_unique_industries(path):
    industries = set()
    file_csv = jobs.read(path)
    for industrie in file_csv:
        if len(industrie["industry"]) != 0:
            industries.add(industrie["industry"])
    return industries


def filter_by_industry(jobs, industry):
    array_filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            array_filter_industry.append(job)
    return array_filter_industry


def get_max_salary(path):
    max = 0
    job_info = jobs.read(path)
    for job in job_info:
        try:
            if len(job["max_salary"]) != 0 and int(job["max_salary"]) > max:
                max = int(job["max_salary"])
        except ValueError as e:
            print(e)
    return max


def get_min_salary(path):
    min = 1000000
    job_info = jobs.read(path)
    for job in job_info:
        try:
            if len(job["min_salary"]) != 0 and int(job["min_salary"]) < min:
                min = int(job["min_salary"])
        except ValueError as e:
            print(e)
    return min


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass
    return result
