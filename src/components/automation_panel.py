import streamlit as st
from utils.ansible_service import AnsibleService
from utils.health_check_service import HealthCheckService
from datetime import datetime

class AutomationPanel:
    def __init__(self):
        self.ansible_service = AnsibleService()
        self.health_check_service = HealthCheckService()

    def render(self):
        st.header("Automation Panel")

        # Create tabs for different sections
        tabs = st.tabs(["Health Checks", "Ansible Playbooks", "Recent Actions"])

        with tabs[0]:
            self.render_health_checks()

        with tabs[1]:
            self.render_playbooks_section()

        with tabs[2]:
            self.render_recent_actions()

    def render_health_checks(self):
        """Render health checks section"""
        st.subheader("System Health Checks")

        # System selection
        selected_system = st.selectbox(
            "Select System",
            self.health_check_service.get_available_systems()
        )

        # Create a form for health check
        with st.form("health_check_form"):
            st.write("Run health check for selected system")
            submitted = st.form_submit_button("Run Health Check")
            
            if submitted:
                try:
                    results = self.health_check_service.run_check(selected_system)
                    
                    # Display results outside the form
                    st.success("Health check completed!")
                    
                    # Display overall status
                    status_color = {
                        "healthy": "green",
                        "warning": "orange",
                        "critical": "red"
                    }[results["status"]]
                    
                    st.markdown(
                        f"<h3 style='color: {status_color}'>Status: {results['status'].upper()}</h3>",
                        unsafe_allow_html=True
                    )

                    # Display checks in an expander
                    with st.expander("Detailed Results", expanded=True):
                        for check in results["checks"]:
                            col1, col2, col3 = st.columns([2, 1, 1])
                            with col1:
                                st.write(check["name"])
                            with col2:
                                st.write(check["value"])
                            with col3:
                                st.write(check["status"])

                except Exception as e:
                    st.error(f"Error running health check: {str(e)}")

    def render_playbooks_section(self):
        """Render available playbooks section"""
        st.subheader("Available Playbooks")

        # Get available playbooks
        playbooks = self.ansible_service.get_available_playbooks()

        # Display each playbook as an expander
        for playbook in playbooks:
            with st.expander(f"{playbook['name']} - {playbook['description']}"):
                # Create form for playbook parameters
                form_id = f"playbook_form_{playbook['id']}"
                with st.form(form_id):
                    params = {}
                    
                    # Generate input fields for required parameters
                    for param in playbook["params"]:
                        param_key = f"param_{playbook['id']}_{param}"
                        params[param] = st.text_input(
                            f"{param.replace('_', ' ').title()}"
                        )

                    # Submit button
                    submitted = st.form_submit_button("Run Playbook")
                    
                    if submitted:
                        try:
                            # Validate all parameters are provided
                            if all(params.values()):
                                result = self.ansible_service.run_playbook(
                                    playbook["id"],
                                    params
                                )
                                st.success("Playbook executed successfully!")
                                st.json(result["output"])
                            else:
                                st.error("Please fill in all required parameters")
                        except Exception as e:
                            st.error(f"Error executing playbook: {str(e)}")

    def render_recent_actions(self):
        """Render recent actions section"""
        st.subheader("Recent Automation Actions")

        # Get recent actions
        actions = self.ansible_service.get_recent_actions()

        if not actions:
            st.info("No recent actions found")
            return

        # Display actions in expandable sections
        for action in actions:
            with st.expander(
                f"{action['playbook_id']} - {action['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}"
            ):
                st.json({
                    "Parameters": action["params"],
                    "Status": action["status"],
                    "Output": action["output"]
                })

    def render_action_status(self, action):
        """Render status for a single action"""
        status_color = {
            "success": "green",
            "failed": "red",
            "running": "blue"
        }.get(action["status"], "gray")

        st.markdown(
            f"""
            <div style='padding: 10px; border-left: 5px solid {status_color};'>
                <h4>{action['playbook_id']}</h4>
                <p>Status: {action['status']}</p>
                <small>Time: {action['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

    def render_custom_automation(self):
        """Render custom automation section"""
        st.subheader("Custom Automation")
        st.info("Custom automation features coming soon!")

    def render_ansible_automation(self):
        st.subheader("Ansible Automation")
        
        # Playbook selection
        playbook = st.selectbox(
            "Select Playbook",
            self.ansible_service.get_available_playbooks()
        )

        # Parameters input
        params = {}
        for param in self.ansible_service.get_playbook_params(playbook):
            params[param] = st.text_input(f"Parameter: {param}")

        if st.button("Run Playbook"):
            with st.spinner("Executing playbook..."):
                result = self.ansible_service.run_playbook(playbook, params)
                st.json(result) 