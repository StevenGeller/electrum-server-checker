name: Pull Request
description: Create a pull request to contribute to the project
title: ""
labels: []
body:
  - type: markdown
    attributes:
      value: |
        Thanks for creating this pull request! Please ensure you've reviewed our contributing guidelines.
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Please provide a detailed description of your changes
      placeholder: What changes does this PR introduce? Why are these changes needed?
    validations:
      required: true
  - type: textarea
    id: testing
    attributes:
      label: Testing
      description: Please describe the tests that you ran to verify your changes
      placeholder: |
        1. How have you tested these changes?
        2. What tests have you added?
        3. How can reviewers verify your changes?
    validations:
      required: true
  - type: checkboxes
    id: checks
    attributes:
      label: Code Quality Checks
      description: Please confirm that you have run the following
      options:
        - label: I have run `black` for code formatting
          required: true
        - label: I have run `isort` for import sorting
          required: true
        - label: I have run `flake8` and addressed any issues
          required: true
        - label: I have added/updated tests as needed
          required: true
        - label: I have updated documentation as needed
          required: true
  - type: textarea
    id: related-issues
    attributes:
      label: Related Issues
      description: Please link any related issues here
      placeholder: "Fixes #123, Relates to #456"
  - type: checkboxes
    id: terms
    attributes:
      label: Code of Conduct
      description: By submitting this PR, you agree to follow our Code of Conduct
      options:
        - label: I agree to follow this project's Code of Conduct
          required: true