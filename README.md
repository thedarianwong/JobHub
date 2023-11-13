# JobHub
## We will get you all the jobs you ever wanted to find..

### Inspiration
The co-op job search can be daunting. Think about how often you input keywords like:
When you are in the co-op job search process. You'll search for 
- Software Engineer Intern 
- Software Engineer Co-op 
- Software Developer Intern 
- Software Developer Co-op 
- Data Engineer Intern 
- Data Engineer Co-op 

...and so on. You diligently place these into platforms like Indeed, LinkedIn, Glassdoor, and more. Initially, enthusiasm fuels your search, but after weeks without success, it can wear you down. 

Enter "_JobHubSFU.com_", where you're greeted by a curated list of job opportunities, aggregated from various platforms based on common search terms. One-click takes you directly to the application. 

Our mission is to ease your transition from student to professional and guide you into the next chapter of your career.

### What's On The Horizon? 
Being newcomers to these technologies, we're still in the blueprint phase. Here's a roadmap:
1. Broaden our horizons by researching more capabilities and tools.
2. Finalize our tech stack and architectural design.
3. Segment the project into sizable tasks.
4. Further dissect these tasks into actionable tickets that can be individually managed.
5. Collaborate during the foundational setup.
6. Build a functional, user-friendly application.
7. Launch to the web.
8. Open our doors to external developer contributions, expanding beyond just CS roles.

In-depth documentation will accompany the project, ensuring that even those with minimal experience can jump in and contribute. It's an exciting venture, especially for those keen on exploring Amazon Web Services (AWS) and the intricacies of software development.

### Potential Extensions:
- **User Profiles**: Tailored by major, experience level, and more.
  - Custom experiences can be curated based on these details.
- **More Platforms**: The more, the merrier.
  - Custom scrapers will be necessary due to unique site structures.
- **Notifications**: Email or messages via AWS SNS for daily updates.
- **Resume Review**: Share your CV and receive constructive feedback (or a gentle roast).

... and countless other possibilities!

For a sneak peek into our architectural vision, check out the preliminary diagram below.

<img width="453" alt="image" src="https://github.com/thedarianwong/JobHub/client/job-aggregator-client/src/jobhub_logo.png>

--------------------------------------------------------------------------------------------------
# JobHub
The transition from academic studies to professional internships is a significant "turning over a new leaf" moment for SFU students. "JobHub" aims to make this transformative journey smoother, ensuring that students can confidently step into the professional world.
## Installation and Run Instructions

### Server Setup

1. Open a terminal and navigate to the server directory:
   ```bash
   cd server/job-server
   pip install Flask Flask-SQLAlchemy
   flask run
   ```
  
2. Open another terminal:
  
  ```bash
  cd client/job-aggregator-client
  npm install
  npm start
  ```

### Frontend: 
Built with React and 'GET' jobs data from server using Axios

### Backend: 
Used Python with JobSpy to built scraper for scraping jobs and export as .csv file
Created Database with SQLite
Used Flask to manipulate and queried needed jobs data
Added route at @app.route('/jobs', methods=['GET'])
\



