**unreleased**

- Replace **show_trace** method by **display_channel**
- Replace **print-screen** method by **screen_dump**
- Allow connection with TCP/IP, LXI and USBTMC interfaces.
- Remove IP address related methods
- Remove calibrate property. The **calibrate** method return the status.
- Remove **get_wave_to_file** and **display_wave** methods  
- Remove logging package dependency
- Remove version constant in Lecroy class
- Remove **show_message** method.
- **get_hardcopy** method return parameters in dictionnary format
- Defined constant classes
- Defined getter: identifier, display, grid, auto_cal, mode
- Defined setter: display, grid, auto_cal, mode
- Move examples to documentation
- Rename lecroy_info utility to lcry_info.


**v0.1.2**
- Correction on a wrong WaitOPC method usage
- Install executable script during package install
- No API modification

**v0.1.1**
- Hotfix. Change project architecture for package installation issue. No functional changes.

**v0.1.0**
- Initial revision
