from mininet.topo import Topo

class ProjectTopo( Topo ):
    "SDN Project Topology for Week 3-8"

    def build( self ):
        # 1. Add Switches (S1 to S6)
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )

        # 2. Add Hosts (H1 to H6)
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )

        # 3. Connect Switches (Inter-switch links)
        # Primary Path Links: S1 -> S2 -> S3 -> S6
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s6 )

        # Alternate Path Links: S1 -> S4 -> S5 -> S6 and S4 -> S6
        self.addLink( s1, s4 )
        self.addLink( s4, s5 )
        self.addLink( s5, s6 )
        self.addLink( s4, s6 )

        # 4. Connect Hosts to Switches
        # Based on diagram in Page 3
        self.addLink( h1, s1 ) # Source
        self.addLink( h2, s6 ) # Destination
        self.addLink( h3, s2 )
        self.addLink( h4, s5 )
        self.addLink( h5, s3 )
        self.addLink( h6, s6 )

# This allows you to run it from the command line
topos = { 'project_topo': ( lambda: ProjectTopo() ) }
