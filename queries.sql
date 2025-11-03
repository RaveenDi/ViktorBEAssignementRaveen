CREATE TABLE Company (
  IdCompany UUID PRIMARY KEY,
  Name VARCHAR(255) NOT NULL
);

CREATE TABLE Employee (
  IdEmployee UUID PRIMARY KEY,
  IdCompany UUID NOT NULL,
  Name VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  IsActive BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (IdCompany) REFERENCES Company(IdCompany)
);

CREATE TABLE Employee (
  IdEmployee UUID PRIMARY KEY, -- This is the manager of the project
  IdCompany UUID NOT NULL,
  Name VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  IsActive BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (IdCompany) REFERENCES Company(IdCompany)
);

-- 1. Get the names of the running Projects
-- A project is running if FinishedAt is NULL
SELECT
  Name
FROM
  Project
WHERE
  FinishedAt IS NULL;


-- 2. Get the number of finished Projects per Company
-- Join Project → Employee → Company and filter where FinishedAt is NOT NULL

SELECT
  C.Name AS CompanyName,
  COUNT(P.IdProject) AS FinishedProjectCount
FROM
  Project P
  INNER JOIN Employee E ON P.IdEmployee = E.IdEmployee
  INNER JOIN Company C ON E.IdCompany = C.IdCompany
WHERE
  P.FinishedAt IS NOT NULL
GROUP BY
  C.Name;


-- 3. Get the Company Names that have 2 or more different Projects with the same Name
-- We group by Company and Project Name, then filter for duplicates

SELECT DISTINCT
  C.Name AS CompanyName
FROM
  Project P
  INNER JOIN Employee E ON P.IdEmployee = E.IdEmployee
  INNER JOIN Company C ON E.IdCompany = C.IdCompany
GROUP BY
  C.IdCompany,
  C.Name,
  P.Name
HAVING
  COUNT(P.IdProject) >= 2;