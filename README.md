 # AggregatePaths

 #### This application processes a text file (`output.txt`) by removing unwanted lines and words, adding desired lines, and then outputs the cleaned and formatted data. The configuration for these operations is specified in a JSON file (`configuration.json`). 

 ## Project Structure

 ```
 AggregatorAndCleanerApp/
 │
 ├── run.py
 ├── output.txt
 ├── README.md
 ├── src/
 │   ├── clear.py
 │   ├── configuration.json
 │   └── aggregator/
 │       └── aggregator.py
 ```

 ## File Descriptions

 - `run.py`: The main script to execute the application.
 - `output.txt`: The input file to be processed.
 - `src/clear.py`: Defines the `cleared` class which uses the `aggregator` to process lines based on the configuration.
 - `src/configuration.json`: Contains the configuration for lines and words to be banned, wanted, and deleted.
 - `src/aggregator/aggregator.py`: Defines the `aggre` class which handles the core line processing logic.

 ## Usage

 1. **Prepare `output.txt`**: Place the content you want to process inside `output.txt`.

 2. **Configure `configuration.json`**: Modify the configuration file to set your desired `wanted`, `banned`, and `delete` words/phrases.

 ```json
 {
 "wanted": [],
 "banned": [".pyc", "deleted:", ".history", "__pycache__", "Untracked", "git add", "git restore", "not staged"],
 "delete": ["modified:", "new file:"]
 }
 ```

 - `wanted`: Lines containing any of these words will be included.
 - `banned`: Lines containing any of these words will be excluded.
 - `delete`: Words to be removed from each line.

 3. **Run the Application**:

 Execute the main script to process the file:

 ```bash
 python run.py
 ```

 4. **Check the Results**: The processed content will overwrite the original `output.txt` file.

 Classes and Methods

 Class `aggre` (Defined in `src/aggregator/aggregator.py`)

 `__init__(self, lines: list[str], banned: list[str] = [''], wanted: list[str] = [''], delete: list[str] = [''])`
 - Initializes with a list of lines and optional banned, wanted, and delete lists.

 `__f_lines(self)`
 - Processes lines by removing newlines, deleting banned words, adding wanted lines, and removing delete words.

 `__f_one_line(self)`
 - Concatenates all processed lines into a single string.

 Class `cleared` (Defined in `src/clear.py`)

 `__init__(self, lines: list[dict], configuration_address: str = "src/configuration.json")`
 - Initializes with a list of dictionaries and an optional path to the configuration file.
 - Uses the `aggre` class for processing lines based on the configuration.

 `__load_json(self, address: str)`
 - Loads and validates the JSON configuration.

 `__check_configuration(self, config : dict)`
 - Validates the presence of required keys in the configuration.

 Configuration

 - The `configuration.json` file should contain three keys: `wanted`, `banned`, and `delete`.
 - If any of these lists are empty, set them as `[""]` in the configuration file.

## Running Tests

To run the tests, navigate to the project directory and use the following command:
```bash
pytest tests/
```

### Test Files

- **tests/test_aggregator.py**: Tests for the `aggre` class in `aggregator.py`.
- **tests/test_clear.py**: Tests for the `cleared` class in `clear.py`.
- **tests/test_run.py**: Tests for the main script `run.py`.
- **tests/conftest.py**: Contains fixtures and configurations used by the test files.

## License

 ### License

 This project is licensed under the GNU General Public License - see the LICENSE file for details.

### Contributing

 1. Fork the repository.
 2. Create a new branch (`git checkout -b feature-branch`).
 3. Commit your changes (`git commit -am 'Add new feature'`).
 4. Push to the branch (`git push origin feature-branch`).
 5. Create a new Pull Request.

 ### Contact

 For any inquiries or feedback, please contact [your-email@example.com].

 ---

 *Note: This README assumes the app is part of a GitHub repository and should be adjusted to reflect the actual repository and contact details.*
