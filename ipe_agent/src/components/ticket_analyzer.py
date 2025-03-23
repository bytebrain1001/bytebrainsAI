import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from services.ticket_analysis_service import TicketAnalysisService
import pandas as pd
from typing import Dict, Any

class TicketAnalyzer:
    def __init__(self):
        self.service = TicketAnalysisService()
        
    def render(self):
        """Render the ticket analysis interface"""
        st.title("Ticket Analysis Dashboard")
        
        # Load data
        df = self.service.load_sample_data()
        
        # Create tabs for different analysis views
        tab1, tab2, tab3 = st.tabs(["Overview", "Trend Analysis", "Content Analysis"])
        
        with tab1:
            self._render_overview(df)
            
        with tab2:
            self._render_trend_analysis(df)
            
        with tab3:
            self._render_content_analysis(df)
    
    def _render_overview(self, df: pd.DataFrame):
        """Render overview statistics and insights"""
        st.header("Overview")
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Tickets", len(df))
            
        with col2:
            open_tickets = len(df[df['status'] == 'Open'])
            st.metric("Open Tickets", open_tickets)
            
        with col3:
            critical_tickets = len(df[df['priority'] == 'Critical'])
            st.metric("Critical Tickets", critical_tickets)
            
        with col4:
            avg_resolution = df['resolution_time'].mean()
            st.metric("Avg Resolution Time (days)", f"{avg_resolution:.1f}")
        
        # Display insights
        st.subheader("Key Insights")
        insights = self.service.generate_insights(df)
        for insight in insights:
            st.info(insight)
        
        # Display priority distribution
        st.subheader("Priority Distribution")
        priority_dist = df['priority'].value_counts()
        fig = px.pie(
            values=priority_dist.values,
            names=priority_dist.index,
            title="Ticket Priority Distribution"
        )
        st.plotly_chart(fig)
    
    def _render_trend_analysis(self, df: pd.DataFrame):
        """Render trend analysis visualizations"""
        st.header("Trend Analysis")
        
        # Get trend data
        trends = self.service.analyze_ticket_trends(df)
        
        # Monthly ticket trends
        st.subheader("Monthly Ticket Volume")
        monthly_counts = trends['monthly_counts']
        # Convert Period to string for plotting
        monthly_counts['month'] = monthly_counts['month'].astype(str)
        fig = px.line(
            monthly_counts,
            x='month',
            y='count',
            title="Monthly Ticket Volume Trend"
        )
        st.plotly_chart(fig)
        
        # Resolution time by priority
        st.subheader("Average Resolution Time by Priority")
        resolution_data = pd.DataFrame({
            'Priority': trends['avg_resolution_time'].keys(),
            'Days': trends['avg_resolution_time'].values()
        })
        fig = px.bar(
            resolution_data,
            x='Priority',
            y='Days',
            title="Average Resolution Time by Priority"
        )
        st.plotly_chart(fig)
        
        # Component distribution
        st.subheader("Tickets by Component")
        component_dist = pd.DataFrame({
            'Component': trends['component_distribution'].keys(),
            'Count': trends['component_distribution'].values()
        })
        fig = px.bar(
            component_dist,
            x='Component',
            y='Count',
            title="Ticket Distribution by Component"
        )
        st.plotly_chart(fig)
    
    def _render_content_analysis(self, df: pd.DataFrame):
        """Render content analysis results"""
        st.header("Content Analysis")
        
        # Get content analysis results
        content_analysis = self.service.analyze_ticket_content(df)
        
        # Display cluster analysis
        st.subheader("Ticket Clusters")
        cluster_terms = content_analysis['cluster_terms']
        
        for cluster, terms in cluster_terms.items():
            with st.expander(f"{cluster} - Top Terms"):
                st.write(", ".join(terms))
        
        # Display sample tickets from each cluster
        st.subheader("Sample Tickets by Cluster")
        df['cluster'] = content_analysis['clusters']
        
        for cluster in range(5):
            cluster_tickets = df[df['cluster'] == cluster].head(3)
            if not cluster_tickets.empty:
                with st.expander(f"Sample Tickets from Cluster {cluster + 1}"):
                    for _, ticket in cluster_tickets.iterrows():
                        st.write(f"**{ticket['title']}**")
                        st.write(f"Priority: {ticket['priority']}")
                        st.write(f"Status: {ticket['status']}")
                        st.write("---") 