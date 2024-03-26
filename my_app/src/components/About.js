import React from 'react';
import './About.css'; // Ensure this CSS file contains the necessary styling

// Import the profile picture from the assets
import profilePic from '/workspaces/gradsearch/grad-job-search/src/components/assets/images/profile.jpg'; // Update the path as needed

const About = () => {
  return (
    <div className="about-container">
      <h1>About Grad Job Search Engine</h1>
      <section aria-labelledby="mission-statement">
        <h2 id="mission-statement">Our Mission</h2>
        <p>
          The Grad Job Search Engine is dedicated to revolutionizing the job
          search experience for recent college graduates. This platform, a
          passion project by Maggie Long, focuses on accessibility and
          navigable design, helping new professionals start their careers.
        </p>
      </section>

      <section aria-labelledby="creator">
        <h2 id="creator">The Creator Behind the Project</h2>
        <img src={profilePic} alt="Maggie Long" className="creator-profile-pic" />
        <p>
          I'm Maggie Long, the sole developer of this platform. My academic
          journey in Humanities, Computing, and Design has fueled my mission to
          create accessible and user-friendly digital experiences.
        </p>
        <p>
          Connect with me on{' '}
          <a
            href="https://www.linkedin.com/in/maggielongg/"
            target="_blank"
            rel="noopener noreferrer"
          >
            LinkedIn
          </a>.
        </p>
      </section>

      <section aria-labelledby="contact-info">
        <h2 id="contact-info">Contact</h2>
        <p>
          For inquiries or collaboration opportunities, please contact me at{' '}
          <a href="mailto:contact@gradjobsearchengine.com">
            contact@gradjobsearchengine.com
          </a>{' '}
          or through my{' '}
          <a
            href="https://www.linkedin.com/in/maggielongg/"
            target="_blank"
            rel="noopener noreferrer"
          >
            LinkedIn profile
          </a>.
        </p>
      </section>
    </div>
  );
};

export default About;